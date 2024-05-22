import socket
import json

host = "127.0.0.1"
port = 9999

socket_c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_c.connect((host, port))

username = input("Enter you username: ")

socket_c.sendto(username.encode("ascii"),(host,port))

def send_request(request):
    socket_c.send(request.encode())

def request_data(query_type, query):
    request = json.dumps({'type': query_type, 'query': query})
    socket_c.send(request.encode())

def receive_response():
    buffer = ''
    while True:
        part = socket_c.recv(4096).decode()
        buffer += part
        try:
            return json.loads(buffer)
        except json.JSONDecodeError:
            continue


def handle_main_menu():
    print("""
            Main Menu:
            [1] Search Headlines
            [2] List of Sources
            [3] Quit
            """)
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        search_headlines()
    elif choice == "2":
        list_of_sources()
    elif choice == "3":
        print("Quit...")
        socket_c.send("exit".encode())
        exit()
    else:
        print("Invalid choice.")


def search_headlines():
    print("=" * 5 ,"Search headlines Menu", "=" * 5)
    print('''
    [1] Search for keywords
    [2] Search by category
    [3] Search by country
    [4] List all new headlines
    [5] Back to the main menu
    ''')
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        search_by_keyword()
    elif choice == "2":
        search_by_category("?category=", "headlines")
    elif choice == "3":
        search_by_country("?country=", "headlines")
    elif choice == "4":
        list_all_headlines()
    elif choice == "5":
        print("Going back to main menu.")
        handle_main_menu()
    else:
        print("Invalid choice.")
        handle_main_menu()

def list_of_sources():
    print("=" * 5, "List of Sources Menu", "=" * 5)
    print('''
        [1] Search by category 
        [2] Search by country
        [3] Search by language
        [4] List all
        [5] Back to the main menu
        ''')
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        search_by_category("/sources?category=", "sources")
    elif choice == "2":
        search_by_country("/sources?country=", "sources")
    elif choice == "3":
        search_by_language()
    elif choice == "4":
        list_all_sources()
    elif choice == "5":
        print("Going back to main menu.")
        handle_main_menu()
    else:
        print("Invalid choice.")
        handle_main_menu()

def search_by_keyword():
    keyword = input("Enter a keyword: ")
    print("Searching by keyword...")
    request_data("headlines", "top-headlines?q={}".format(keyword))

def search_by_category(url, query_type):
    categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    print("Categories: business, entertainment, general, health, science, sports, technology")
    category = input("Enter a category: ")
    print("Searching by category...\n")
    path = url + category
    if category in categories:
        request_data(query_type, "top-headlines{}".format(path))
    else:
        print("Invalid Choice")
        handle_main_menu()
def search_by_country(url, query_type):
    countries = ["au", "nz", "ca", "ae", "sa", "gb", "us", "eg", "ma"]
    print("Countries: au, nz, ca, ae, sa, gb, us, eg, ma")
    country = input("Enter a country: ")
    print("Searching by country...")
    if country in countries:
        path = url + country
        request_data(query_type, "top-headlines{}".format(path))
    else:
        print("Invalid Choice")
        handle_main_menu()


def search_by_language():
    languages = ["ar", "en"]
    print("Languages: ar (Arabic) , en (English)")
    language = input("Enter a language: ")
    if language in languages:
        request_data("sources", "top-headlines/sources?language={}".format(language))
    else:
        print("Invalid Choice")
        handle_main_menu()


def list_all_headlines():
    request_data("headlines", "top-headlines?q=\" \"")
    print("Searching...")

def list_all_sources():
    request_data("sources", "top-headlines/sources?")
    print("Searching...")

def display_list(data, query_type):
    if query_type == 'headlines':
        headlines = data.get("data", [])
        for idx, article in enumerate(headlines, 1):
            print(f"{idx}. Source: {article['source_name']}, Author: {article['author']}, Title: {article['title']}")
    elif query_type == 'sources':
        sources = data.get("data", [])
        for idx, source in enumerate(sources, 1):
            print(f"{idx}. Source: {source['source_name']}\n")


def display_details(data, query_type, index):
    response = data.get("data", [])
    item = response[index]
    if query_type == 'headlines':
        print(f"Source: {item['source_name']}")
        print(f"Author: {item['author']}")
        print(f"Title: {item['title']}")
        print(f"URL: {item['url']}")
        print(f"Description: {item['description']}")
        print(f"Publish Date: {item['publish_date']}")
        print(f"Publish Time: {item['publish_time']}")
    elif query_type == 'sources':
        print(f"Source: {item['source_name']}")
        print(f"Country: {item['country']}")
        print(f"Description: {item['description']}")
        print(f"URL: {item['url']}")
        print(f"Category: {item['category']}")
        print(f"Language: {item['language']}")
def main():
    while True:
        if handle_main_menu() is False:
            break

        response = receive_response()

        display_list(response, response.get('type'))

        data = response.get("data", [])
        if len(data) != 0:
            index = int(input("Enter the number of the item to view details: ")) - 1
            if 0 <= index < len(data):
                display_details(response, response.get('type'), index)
            else:
                print("Invalid selection.")
        else:
            print("There is no data")

if __name__ == "__main__":
    main()