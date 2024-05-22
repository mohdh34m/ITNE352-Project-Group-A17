import socket
import threading
import json
import requests

api_key = ""  # Replace with your API key

# Function to retrieve news data from NewsAPI
def get_news(client_socket, query, request_type):
    try:
        params = {
            'pageSize': 15
        }

        api_result = requests.get('https://newsapi.org/v2/{}&apiKey={}'.format(query, api_key), params=params)

        if api_result.status_code == 200:
            news_data = api_result.json()
            if request_type == "headlines":
                articles = [
                    {
                        'source_name': article['source']['name'],
                        'author': article.get('author'),
                        'title': article.get('title'),
                        'url': article.get('url'),
                        'description': article.get('description'),
                        'publish_date': article.get('publishedAt')[:10],
                        'publish_time': article.get('publishedAt')[11:19]
                    } for article in news_data.get('articles', [])
                ]
                client_socket.send(json.dumps({'type': 'headlines', 'data': articles}).encode())


            elif request_type == "sources":
               sources = [
                    {
                        'source_name': source['name'],
                        'country': source.get('country'),
                        'description': source.get('description'),
                        'url': source.get('url'),
                        'category': source.get('category'),
                        'language': source.get('language')
                    } for source in news_data.get('sources', [])
                ]
               client_socket.send(json.dumps({'type': 'sources', 'data': sources}).encode())
        else:
            print(f"Error getting data from API. Status Code: {api_result.status_code}")
            return []
    except requests.RequestException as e:
        print(f"Error making API request: {e}")
        return []


# Function to handle client connections

def handle_client(client_socket, client_name, api_key):
    print(f"Connection from {client_name} has been established!")

    try:
        while True:
            request = client_socket.recv(1024).decode()
            if request == "exit":
                print(f"Client {client_name} has disconnected.")
                client_socket.close()

            request_data = json.loads(request)
            query_type = request_data.get('type')
            query = request_data.get('query')

            print(f"Request From {client_name}: Query: {query}, Type: {query_type}")
            get_news(client_socket, query, query_type)

    except Exception as e:
        print(f"Error handling client {client_name}: {e}")


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
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_name, api_key))
        client_thread.start()


if __name__ == "__main__":
    main()
