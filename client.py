import socket

def start_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("192.168.1.7", 12345))

# Receive the message from the server (it’s usually a good idea to set a buffer size)
    data = client_socket.recv(1024)

# Print the message from the server
    print(f"Received from server: {data.decode()}")

# Close the client connection
    client_socket.close()

# This ensures the client only runs when this script is executed directly
if __name__ == "__main__":
    start_client()