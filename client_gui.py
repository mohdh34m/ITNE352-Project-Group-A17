import socket
import json
import customtkinter as ctk
from tkinter import Listbox, END, VERTICAL, RIGHT, LEFT, Y, BOTH
from PIL import Image
from CTkMessagebox import CTkMessagebox


host = "127.0.0.1"
port = 9999

socket_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_c.connect((host, port))

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

def quit():
    msg = CTkMessagebox(title="Exit?", message="Do you want to close the program?",
                        icon="question", option_1="Cancel", option_2="Yes",
                        font= ("FiraCode Nerd Font Mono SemBd", 24),
                        button_hover_color="#6541f5",
                        button_color="#1a1a2f",
                        button_text_color="#ffffff",
                        fg_color="#1a1a2f",
                        bg_color="#1a1a2f"
                        )
    response = msg.get()
    
    if response=="Yes":
        socket_c.send("exit".encode())
        root.quit()

def show_error(title, message):
    CTkMessagebox(title=title, message=message, icon="cancel",
                        font= ("FiraCode Nerd Font Mono SemBd", 24),
                        button_hover_color="#6541f5",
                        button_color="#1a1a2f",
                        button_text_color="#ffffff",
                        fg_color="#1a1a2f",
                        bg_color="#1a1a2f")

country_logo = ctk.CTkImage(light_image=Image.open("./images/flag.png"))
category_logo = ctk.CTkImage(light_image=Image.open("./images/category.png"))
list_logo = ctk.CTkImage(light_image=Image.open("./images/list.png"))
back_logo = ctk.CTkImage(light_image=Image.open("./images/angle-double-left.png"))

def main_menu():
    clear_frame()
    ctk.CTkLabel(main_frame, text="Main Menu", font=("FiraCode Nerd Font Mono SemBd", 24), text_color="#ffffff").pack(pady=20)
    ctk.CTkButton(main_frame, text="Search Headlines", command=search_headlines, height=40,
                    font= ("FiraCode Nerd Font Mono SemBd", 24),
                    text_color="#ffffff",
                    hover= True,
                    hover_color= "#6541f5",
                    border_width=2,
                    border_color="#6541f5",
                    corner_radius=20,
                    fg_color= "#1a1a2f",
                    image=ctk.CTkImage(light_image=Image.open("./images/news.png"))).pack(fill=ctk.X, padx=20, pady=10)
    ctk.CTkButton(main_frame, text="List of Sources", command=list_of_sources, height=40,
                    font= ("FiraCode Nerd Font Mono SemBd", 24),
                    text_color="#ffffff",
                    hover= True,
                    hover_color= "#6541f5",
                    border_width=2,
                    border_color="#6541f5",
                    corner_radius=20,
                    fg_color= "#1a1a2f",
                    image=ctk.CTkImage(light_image=Image.open("./images/source-document.png"))).pack(fill=ctk.X, padx=20, pady=10)
    ctk.CTkButton(main_frame, text="Quit", command=quit, height=40,
                    font= ("FiraCode Nerd Font Mono SemBd", 24),
                    text_color="#ffffff",
                    hover= True,
                    hover_color= "#6541f5",
                    border_width=2,
                    border_color="#6541f5",
                    corner_radius=20,
                    fg_color= "#1a1a2f",
                    image=ctk.CTkImage(light_image=Image.open("./images/circle-xmark.png")),).pack(fill=ctk.X, padx=20, pady=10)

def search_headlines():
    clear_frame()
    ctk.CTkLabel(main_frame, text="Search Headlines Menu", font=("FiraCode Nerd Font Mono SemBd", 24)).pack(pady=20)
    ctk.CTkButton(main_frame, text="Search for keywords", command=search_by_keyword, height=40,
                    font= ("FiraCode Nerd Font Mono SemBd", 24),
                    text_color="white",
                    hover= True,
                    hover_color= "#ffb557",
                    border_width=2,
                    corner_radius=20,
                    border_color= "#ffb557", 
                    fg_color= "#1a1a2f",
                    image=ctk.CTkImage(light_image=Image.open("./images/search.png"))).pack(fill=ctk.X, padx=20, pady=10)
    ctk.CTkButton(main_frame, text="Search by category", command=lambda: search_by_category("?category=", "headlines"), height=40,
                    font= ("FiraCode Nerd Font Mono SemBd", 24),
                    text_color="white",
                    hover= True,
                    hover_color= "#ffb557",
                    border_width=2,
                    corner_radius=20,
                    border_color= "#ffb557", 
                    fg_color= "#1a1a2f",
                    image=category_logo).pack(fill=ctk.X, padx=20, pady=10)
    ctk.CTkButton(main_frame, text="Search by country", command=lambda: search_by_country("?country=", "headlines"), height=40,
                    font= ("FiraCode Nerd Font Mono SemBd", 24),
                    text_color="white",
                    hover= True,
                    hover_color= "#ffb557",
                    border_width=2,
                    corner_radius=20,
                    border_color= "#ffb557", 
                    fg_color= "#1a1a2f",
                    image=country_logo).pack(fill=ctk.X, padx=20, pady=10)
    ctk.CTkButton(main_frame, text="List all new headlines", command=list_all_headlines, height=40,
                    font= ("FiraCode Nerd Font Mono SemBd", 24),
                    text_color="white",
                    hover= True,
                    hover_color= "#ffb557",
                    border_width=2,
                    corner_radius=20,
                    border_color= "#ffb557", 
                    fg_color= "#1a1a2f",
                    image=list_logo).pack(fill=ctk.X, padx=20, pady=10)
    ctk.CTkButton(main_frame, text="Back to Main Menu", command=main_menu, height=40,
                    font= ("FiraCode Nerd Font Mono SemBd", 24),
                    text_color="white",
                    hover= True,
                    hover_color= "#ffb557",
                    border_width=2,
                    corner_radius=20,
                    border_color= "#ffb557", 
                    fg_color= "#1a1a2f",
                    image=back_logo).pack(fill=ctk.X, padx=20, pady=10)

def list_of_sources():
    clear_frame()
    ctk.CTkLabel(main_frame, text="List of Sources Menu", font=("FiraCode Nerd Font Mono SemBd", 24)).pack(pady=20)
    ctk.CTkButton(main_frame, text="Search by category", command=lambda: search_by_category("/sources?category=", "sources"), height=40,
                    font= ("FiraCode Nerd Font Mono SemBd", 24),
                    text_color="white",
                    hover= True,
                    hover_color= "#ffb557",
                    border_width=2,
                    corner_radius=20,
                    border_color= "#ffb557", 
                    fg_color= "#1a1a2f",
                    image=category_logo).pack(fill=ctk.X, padx=20, pady=10)
    ctk.CTkButton(main_frame, text="Search by country", command=lambda: search_by_country("/sources?country=", "sources"), height=40,
                    font= ("FiraCode Nerd Font Mono SemBd", 24),
                    text_color="white",
                    hover= True,
                    hover_color= "#ffb557",
                    border_width=2,
                    corner_radius=20,
                    border_color= "#ffb557", 
                    fg_color= "#1a1a2f",
                    image=country_logo).pack(fill=ctk.X, padx=20, pady=10)
    ctk.CTkButton(main_frame, text="Search by language", command=search_by_language, height=40,
                    font= ("FiraCode Nerd Font Mono SemBd", 24),
                    text_color="white",
                    hover= True,
                    hover_color= "#ffb557",
                    border_width=2,
                    corner_radius=20,
                    border_color= "#ffb557", 
                    fg_color= "#1a1a2f",
                    image=ctk.CTkImage(light_image=Image.open("./images/language.png"))).pack(fill=ctk.X, padx=20, pady=10)
    ctk.CTkButton(main_frame, text="List all", command=list_all_sources, height=40,
                    font= ("FiraCode Nerd Font Mono SemBd", 24),
                    text_color="white",
                    hover= True,
                    hover_color= "#ffb557",
                    border_width=2,
                    corner_radius=20,
                    border_color= "#ffb557", 
                    fg_color= "#1a1a2f",
                    image=list_logo).pack(fill=ctk.X, padx=20, pady=10)
    ctk.CTkButton(main_frame, text="Back to Main Menu", command=main_menu, height=40,
                    font= ("FiraCode Nerd Font Mono SemBd", 24),
                    text_color="white",
                    hover= True,
                    hover_color= "#ffb557",
                    border_width=2,
                    corner_radius=20,
                    border_color= "#ffb557", 
                    fg_color= "#1a1a2f",
                    image=back_logo).pack(fill=ctk.X, padx=20, pady=10)

def search_by_keyword():
    keyword = ctk.CTkInputDialog(title="Search by Keyword", text="Enter a keyword:",
                                font=("FiraCode Nerd Font Mono SemBd", 24),
                                fg_color="#1a1a2f",
                                button_fg_color="#1a1a2f",
                                button_text_color="#ffffff",
                                entry_fg_color="#1a1a2f",
                                entry_border_color="#ffffff",
                                entry_text_color="#6541f5",
                                button_hover_color="#6541f5").get_input()
    if keyword:
        request_data("headlines", f"top-headlines?q={keyword}")
        display_list("headlines")

def search_by_category(url, query_type):
    categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    category = ctk.CTkInputDialog(title="Search by Category", text="Enter a category:\n" + ", ".join(categories),
                                font=("FiraCode Nerd Font Mono SemBd", 24),
                                fg_color="#1a1a2f",
                                button_fg_color="#1a1a2f",
                                button_text_color="#ffffff",
                                entry_fg_color="#1a1a2f",
                                entry_border_color="#ffffff",
                                entry_text_color="#6541f5",
                                button_hover_color="#6541f5").get_input()
    if category in categories:
        request_data(query_type, f"top-headlines{url}{category}")
        display_list(query_type)
    else:
        show_error("Error", "Invalid category")

def search_by_country(url, query_type):
    countries = ["au", "nz", "ca", "ae", "sa", "gb", "us", "eg", "ma"]
    country = ctk.CTkInputDialog(title="Search by Country", text="Enter a country code:\n" + ", ".join(countries),
                                font=("FiraCode Nerd Font Mono SemBd", 24),
                                fg_color="#1a1a2f",
                                button_fg_color="#1a1a2f",
                                button_text_color="#ffffff",
                                entry_fg_color="#1a1a2f",
                                entry_border_color="#ffffff",
                                entry_text_color="#6541f5",
                                button_hover_color="#6541f5").get_input()
    if country in countries:
        request_data(query_type, f"top-headlines{url}{country}")
        display_list(query_type)
    else:
        show_error("Error", "Invalid country")

def search_by_language():
    languages = ["ar", "en"]
    language = ctk.CTkInputDialog(title="Search by Language", text="Enter a language code:\n" + ", ".join(languages),
                                font=("FiraCode Nerd Font Mono SemBd", 24),
                                fg_color="#1a1a2f",
                                button_fg_color="#1a1a2f",
                                button_text_color="#ffffff",
                                entry_fg_color="#1a1a2f",
                                entry_border_color="#ffffff",
                                entry_text_color="#6541f5",
                                button_hover_color="#6541f5").get_input()
    if language in languages:
        request_data("sources", f"top-headlines/sources?language={language}")
        display_list("sources")
    else:
        show_error("Error", "Invalid language")

def list_all_headlines():
    request_data("headlines", "top-headlines?q=\" \"")
    display_list("headlines")

def list_all_sources():
    request_data("sources", "top-headlines/sources?")
    display_list("sources")

def display_list(query_type):
    response = receive_response()
    data = response.get("data", [])
    clear_frame()

    ctk.CTkLabel(main_frame, text="Results", font=("FiraCode Nerd Font Mono SemBd", 24)).pack(pady=20)

    listbox_frame = ctk.CTkFrame(main_frame)
    listbox_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
    
    listbox = Listbox(listbox_frame, activestyle='dotbox', font=("FiraCode Nerd Font Mono SemBd", 14), selectbackground="#6541f5")
    listbox.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = ctk.CTkScrollbar(listbox_frame, orientation=VERTICAL, command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox.config(yscrollcommand=scrollbar.set)

    if query_type == 'headlines':
        for idx, article in enumerate(data):
            listbox.insert(END, f"{idx + 1}. {article['title']}")

    elif query_type == 'sources':
        for idx, source in enumerate(data):
            listbox.insert(END, f"{idx + 1}. {source['source_name']}")

    def on_select(event):
        selected_index = listbox.curselection()
        if selected_index:
            index = selected_index[0]
            display_details(response, query_type, index)

    listbox.bind('<<ListboxSelect>>', on_select)
    ctk.CTkButton(main_frame, text="Back to Main Menu", command=main_menu, height=40,
                    font= ("FiraCode Nerd Font Mono SemBd", 24),
                    text_color="#ffffff",
                    hover= True,
                    hover_color= "#6541f5",
                    border_width=2,
                    border_color="#6541f5",
                    corner_radius=20,
                    fg_color= "#1a1a2f").pack(fill=ctk.X, padx=20, pady=10)

def display_details(data, query_type, index):
    item = data.get("data", [])[index]
    details = ""
    if query_type == 'headlines':
        details = (
            f"Source: {item['source_name']}\n\n"
            f"Author: {item['author']}\n\n"
            f"Title: {item['title']}\n\n"
            f"URL: {item['url']}\n\n"
            f"Description: {item['description']}\n\n"
            f"Publish Date: {item['publish_date']}\n\n"
            f"Publish Time: {item['publish_time']}"
        )
    elif query_type == 'sources':
        details = (
            f"Source: {item['source_name']}\n\n"
            f"Country: {item['country']}\n\n"
            f"Description: {item['description']}\n\n"
            f"URL: {item['url']}\n\n"
            f"Category: {item['category']}\n\n"
            f"Language: {item['language']}"
        )

    details_window = ctk.CTkToplevel(root)
    details_window.title("Details")
    details_window.geometry("500x400")

    details_text = ctk.CTkTextbox(details_window, wrap='word', font=("FiraCode Nerd Font Mono SemBd", 14))
    details_text.pack(expand=True, fill=BOTH, padx=20, pady=20)
    details_text.insert('1.0', details)
    details_text.configure(state='disabled')

def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()



root = ctk.CTk()
root.title("News App")
root.geometry("1100x580")
root.after(201, lambda :root.iconbitmap('./images/world-news.ico'))

main_frame = ctk.CTkFrame(root, fg_color="#1a1a2f")
main_frame.pack(fill=BOTH, expand=True)


username = ctk.CTkInputDialog(title="Username", text="Enter your username:",
                              font=("FiraCode Nerd Font Mono SemBd", 24),
                              fg_color="#1a1a2f",
                              button_fg_color="#1a1a2f",
                              button_text_color="#ffffff",
                              entry_fg_color="#1a1a2f",
                              entry_border_color="#ffffff",
                              entry_text_color="#6541f5",
                              button_hover_color="#6541f5").get_input()
socket_c.sendto(username.encode("ascii"), (host, port))

main_menu()

root.mainloop()
