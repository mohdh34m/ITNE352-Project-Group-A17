# ITNE352-Project-Group-A17

# Project Title

Multithreaded News Client/Server Information System

## Project Description

The News Exchange System is a client-server application that allows users to retrieve news updates from NewsAPI.org. The system consists of two main components: a server script responsible for fetching news data and responding to client requests, and a client script that enables users to interact with the server and retrieve news information.

## Semester

Spring 2024

## Group

- **Group Name:** ITNE352 Project – Group A17
- **Course Code:** ITNE352
- **Section:** 1
- **Student Names:** [MOHAMED JASIM ALI HASAN | 202104724] [IBRAHIM SALAH MOHAMED AHMED | 202105795]

## Table of Contents

1. [Requirements](#Requirements)
2. [How to Run](#How-to-Run)
3. [The Scripts](#The-Scripts)
4. [Additional Concept](#Additional-Concept)
5. [Acknowledgments](#Acknowledgments)
6. [Conclusion](#Conclusion)
7. [Resources](#Resources)


## Requirements

To set up and run the project in a local environment, follow these steps:

1. Install Python if not already installed (https://www.python.org/downloads/)
2. Clone the repository to your local machine: `git clone https://github.com/mohdh34m/ITNE352-Project-Group-A17`
3. Navigate to the project directory: `cd ITNE352-Project-Group-A17`
4. Install required dependencies: `pip install -r requirements.txt`
5. Obtain a NewsAPI API key from https://newsapi.org/ and replace `"YOUR_NEWSAPI_API_KEY"` in the server script with your actual API key.

## How to Run

To run the system:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Start the server by running `python CreateServer.py`.
4. In another terminal or command prompt, start the client by running `python Client.py`.
5. Follow the instructions on the client-side interface to interact with the server and retrieve news information.

To run the system with GUI:

1. Ensure you have completed all steps in the  [Requirements](#Requirements) section.
2. Navigate to the project directory.
3. Start the server by running python CreateServer.py.
4. In another terminal or command prompt, start the GUI client by running python `client_gui.py`.

## The Scripts

### Server Script (CreateServer.py)

- The server script is responsible for handling client connections, fetching news data from NewsAPI.org, and responding to client requests.

Main functionalities:
- Handles client connections using sockets and threading.
- Retrieves news data from NewsAPI.org using the `requests` library.
- Parses client requests and sends appropriate responses back.


### Client Script (Client.py)

- The client script allows users to interact with the server and retrieve news information.

Main functionalities:
- Establishes connection with the server using sockets.
- Provides a menu-driven interface for users to search headlines, list sources, and quit.


## Additional Concept

- Socket Programming: Using Python's socket module to communicate between client and server over a network.

- Multithreading: Using multithreading techniques to handle several client connections simultaneously ensures responsiveness and efficiency.

- API Integration: Using NewsAPI.org to retrieve real-time news data, showing the incorporation of external APIs into the project.

## Acknowledgments

- This project could not have been completed without the wonderful resources and assistance offered by NewsAPI.org. Their extensive and up-to-date news database serves as the foundation of our application, allowing users to easily obtain current and relevant news information.

## Conclusion

- In Conclusion, the development of the News Socket Client/Server System marks a significant step toward mastering key concepts in network programming, API integration, and client-server architecture. The project exhibits a comprehensive approach to developing robust and scalable software solutions by carefully implementing error handling, logging, serialization, threading, and user interface enhancement.


## Resources

- **NewsAPI:**
   - Documentation: [NewsAPI Documentation](https://newsapi.org/docs)
   - Description: The official documentation for NewsAPI.org.

- **CustomTkinter:**
   - Documentation: [CustomTkinter Documentation](https://customtkinter.tomschimansky.com/documentation/)
   - Description: CustomTkinter is an extension of the Tkinter GUI toolkit in Python.

- **Tkinter:**
   - Documentation: [Tkinter Documentation](https://docs.python.org/3/library/tk.html)
   - Description: Tkinter is the standard GUI toolkit for Python, and its documentation is part of the official Python documentation.

