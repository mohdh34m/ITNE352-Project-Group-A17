import socket

host = "127.0.0.1"
port = 9999

socket_c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_c.connect((host, port))

username = input("Enter you username: ")

socket_c.sendto(username.encode("ascii"),(host,port))

def handle_main_menu(choice):
    if choice == "1":
        search_headlines()
    elif choice == "2":
        list_of_sources()
    elif choice == "3":
        print("Quit...")
        return False
    else:
        print("Invalid choice.")
    return True

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
        category = input("Enter a category: ")
        search_by_category(category, "?category=")
    elif choice == "3":
        country = input("Enter a country: ")
        search_by_country(country, "?country=")
    elif choice == "4":
        list_all_headlines()
    elif choice == "5":
        print("Going back")
    else:
        print("Invalid choice.")

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
        category = input("Enter a category: ")
        search_by_category(category, "/sources?category=")
    elif choice == "2":
        country = input("Enter a country: ")
        search_by_country(country, "/sources?country=")
    elif choice == "3":
        search_by_language()
    elif choice == "4":
        list_all_sources()
    elif choice == "5":
        print("Going back")
    else:
        print("Invalid choice.")

def search_by_keyword():
    keyword = input("Enter a keyword: ")
    print("Searching by keyword...")
    print("?q={}".format(keyword))

def search_by_category(category, url):
    categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    print("Searching by category...\n")
    print("Categories: business, entertainment, general, health, science, sports, technology")
    path = url + category
    if category in categories:
        print("top-headlines{}".format(path))
    else:
        print("Invalid Choice")
def search_by_country(country, url):
    countries = ["au", "nz", "ca", "ae", "sa", "gb", "us", "eg", "ma"]
    print("Searching by country...")
    if country in countries:
        path = url + country
        print("top-headlines{}".format(path))
    else:
        print("Invalid Choice")

def search_by_language():
    languages = ["ar", "en"]
    print("Languages: ar (Arabic) , en (English)")
    language = input("Enter a language: ")
    if language in languages:
        print("top-headlines/sources?language={}".format(language))
    else:
        print("Invalid choice.")

def list_all_headlines():
    print("Listing all news headlines...")

def list_all_sources():
    print("Listing all sources...")


def main():
    while True:
        print("""
        Main Menu:
        [1] Search Headlines
        [2] List of Sources
        [3] Quit
        """)
        choice = input("Enter your choice (1-3): ")
        if not handle_main_menu(choice):
            break

if __name__ == "__main__":
    main()