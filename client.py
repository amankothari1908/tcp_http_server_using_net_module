import socket

print("starting new client: client 1")

HOST = "localhost"

PORT = 3000 # port of our server to connect

client_socket = socket.socket()

client_socket.connect((HOST,PORT))

client_socket.sendall(b"Hello from client 1")

response_from_server = client_socket.recv(2048)

print("data received by by server is",response_from_server)