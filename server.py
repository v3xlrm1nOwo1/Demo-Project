import threading
import socket
import sqlite3

# addr
host = "127.0.0.1" # localhost
port = 1234


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


def searching():
    pass


def add():
    pass

