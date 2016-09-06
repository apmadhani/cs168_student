import sys
import socket
client_socket = socket.socket()
client_socket.connect((sys.argv[1], int(sys.argv[2])))
client_socket.send("Harambe is love. Harambe is life.")
client_socket.close()