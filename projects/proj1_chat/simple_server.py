import sys
import socket

server_socket = socket.socket()
port = int(sys.argv[1])
server_socket.bind(("0.0.0.0", port))
server_socket.listen(5)
while True:
    (new_sock, address) = server_socket.accept()
    dat = new_sock.recv(200)
    print(dat)