import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("Connection closed")
                break
            print(f"\nServer: {data.decode()}")
        except:
            print("Error receiving data from server")
            break



def start_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.daemon = True  # Optional: ends when main thread ends
    receive_thread.start()

    while True:
        messages = input("You: ")
        if messages.lower() == "exit":
            print("Closing connection")
            client_socket.close()
            break
        client_socket.send(messages.encode())


# This ensures the client only runs when this script is executed directly
if __name__ == "__main__":
    start_client()