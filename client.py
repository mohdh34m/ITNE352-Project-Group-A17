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
        search_by_category()
    elif choice == "3":
        search_by_country()
    elif choice == "4":
        list_all_headlines()
    elif choice == "5":
        print("Going back")
    else:
        print("Invalid choice.")

def list_of_sources():
    print("Sources")

def search_by_keyword():
    keyword = input("Enter a keyword: ")
    print("Searching by keyword...")
    print("q={}".format(keyword))

def search_by_category():
    categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    print("Searching by category...\n")
    print("Categories: business, entertainment, general, health, science, sports, technology")
    category = input("Enter a category: ")
    if category in categories:
        print("top-headlines?category={}".format(category))
    else:
        print("Invalid Choice")
def search_by_country():
    country = input("Enter a country: ")
    print("Searching by country...")
    print("top-headlines?country={}".format(country))

def list_all_headlines():
    print("Listing all news headlines...")


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