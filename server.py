import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Print server status
    print("Server is starting...")

    server_socket.bind(("192.168.1.7", 12345))
    server_socket.listen()

# Print server status
    print("Server started, now listening for connections...")

# Accept a connection from the client
    client_socket, client_address = server_socket.accept()

# Print the client's address (for debug purposes)
    print(f"Connected by {client_address}")

# Send a message to the client
    client_socket.sendall(b"Hello, Client!")

# Close the connection (optional at this point)
    client_socket.close()

# This block ensures that the server only runs when this script is executed directly
if __name__ == "__main__":
    start_server()