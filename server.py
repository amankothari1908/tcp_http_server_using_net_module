import socket
import threading

def connect_a_client(conn , addr):
    print("New client has been connected")
    data = conn.recv(2048)
    print("Data received from client",data)
    conn.sendall(b"Data is received by server")

HOST = "localhost"

PORT = 3000

# create a new socket object
server_socket = socket.socket()

# bind the socket object to the host and port
server_socket.bind((HOST,PORT))

# start listening for new connection
server_socket.listen()

print("server is listening on ",HOST ,PORT)

while True:
    # wait for new connection acceptance
    conn, addr = server_socket.accept()

    # preparing the thread
    t = threading.Thread(target=connect_a_client, args=(conn,addr))

    # starting the thread
    t.start()
