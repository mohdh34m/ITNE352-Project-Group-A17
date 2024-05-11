import socket

host = "127.0.0.1"
port = 49999

socket_c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_c.connect((host, port))

username = input("Enter you username: ")

socket_c.sendto(username.encode("ascii"),(host,port))

print("The request has been sent")

socket_c.close()