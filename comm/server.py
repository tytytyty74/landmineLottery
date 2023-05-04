import socket
from _thread import *
import sys

server = "IPV4 ADDRESS HERE" #input local ip addr
port = 5555  #use accessible port

#type of connection, initialize
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#try to connect port to ip/server
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

#2 can be removed
s.listen(2)
print("Waiting for a connection, Server Started")


def threaded_client(conn, player):
    conn.send(str.encode("Connected"))
    reply = ""


    while True:
        #try to receive data, 2048 is bits, may need to be increased
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            #break if no data
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
#continuously look for connections
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1