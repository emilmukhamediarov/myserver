import socket
import threading

def handle_client(client_socket, client_threads, thread_lock, client_address):
    """Handle a client connection"""
    try:
        while True: # Keep connection alive for multiple messages
            message = client_socket.recv(1024)
            if not message: #Client disconnected
                break
            print(f"Received from {client_address}: {message.decode()}")
            reply = "Message received"
            client_socket.send(reply.encode())
    except ConnectionResetError:
        print("Client disconnected abruptly")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        with thread_lock: #Thread-safe removal
            client_threads.remove(threading.current_thread())
        client_socket.close()
        print("Connection closed")

def start_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    server_socket.settimeout(5.0)

    client_threads = []
    thread_lock = threading.Lock()

    print("Server started, now listening for connections (timeout = 5 seconds). Press Ctrl + C to stop.")

    try:
        while True:
            try:
                client_socket, client_address = server_socket.accept()
                print(f"Connection established with {client_address}!")

                #Handle client in a new thread
                client_thread = threading.Thread(target=handle_client, args=(client_socket, client_threads, thread_lock, client_address))
                with thread_lock: #I am using this now, others wait.
                    client_threads.append(client_thread)
                # Lock is automatically released here
                client_thread.start()

            except socket.timeout:
                if len(client_threads) == 0:
                    print("\n[Timeout] No clients connected... (waiting)")
                    # You can add periodic tasks here
                continue

    except KeyboardInterrupt:
        print("\nServer shutting down...")
        server_socket.close()

        for thread in client_threads:
            thread.join(timeout=1.0) #Wait up to 1 sec per thread

    print("Server stopped.")


if __name__ == "__main__":
    start_server()
