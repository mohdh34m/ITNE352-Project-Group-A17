import socket

sock_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock_s.bind(("127.0.0.1", 49999))

sock_s.listen(3)

sock_a, address = sock_s.accept()

data = sock_a.recv(1024)

print('Accepted request from:', data.decode('ascii'), "with IP:", address[0] ,'with port number', address[1])

sock_a.close()
