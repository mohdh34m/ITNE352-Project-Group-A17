import socket
import threading
import json

# Function to handle client connections
def handle_client(client_socket, client_name):
    # Display client connection
    print(f"Accepted connection from {client_name}")

    # Receive client requests
    while True:
        request = client_socket.recv(1024).decode()

        # Process client request
        if request:
            # Parse request and retrieve data from NewsAPI
            # Save data to JSON file
            # Send list of results to client

            # Example: Sending data to client
            data = {"title": "Sample News", "source": "Sample Source"}
            client_socket.send(json.dumps(data).encode())

    # Close client connection
    print(f"Disconnected from {client_name}")
    client_socket.close()

# Main server function
def main():
    # Server configuration
    host = '127.0.0.1'  # localhost
    port = 9999

    # Create socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket to address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(3)  # Max 3 simultaneous connections

    print("Server listening on port", port)

    # Accept incoming connections and create threads
    while True:
        client_socket, client_address = server_socket.accept()
        client_name = client_socket.recv(1024).decode()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_name))
        client_thread.start()

if __name__ == "__main__":
    main()
