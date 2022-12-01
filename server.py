import threading
import socket
import sqlite3

# addr
host = "127.0.0.1" # localhost
port = 1234

con = sqlite3.connect("Demo.db")
cur = con.cursor()
cur.execute("CREATE TABLE info(first_name, last_name, addr, academic year,semester,Tel)")



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


def searching():
    pass


def add():
    pass

