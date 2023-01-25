import subprocess
import socket
import os

HOST = socket.gethostname() # localhost
PORT = 1234
address = (HOST, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)


def send(msg):
    return str(msg).rjust(1024, " ").encode("utf-8")

def recv():
    return client.recv(1024).decode("utf-8").strip()

while True:
    print(">>>> start <<<<")
    msg = recv()
    print(f"msg: {msg}")
    print("End")

    if msg == "singup or login":
        opration = input(">>> Slect singup or login: ")
        print(opration)
        client.sendall(send(opration))

    elif msg == "name":
        name = input(">>> Enter username: ")
        client.sendall(send(name))

    elif msg == "email":
        email = input(">>> Enter your email: ")
        client.sendall(send(email))

    elif msg == "password":
        password = input(">>> password:\n1 - lowercase alphabets\n2 - uppercase alphabets\n3 - the mentioned special characters\n4 - digits\n>>> Enter your Password: ")
        client.sendall(send(password))

    elif msg == "select game":
        print()
        game = input(">>> Select From This:\n1 - Tic Tac Toe\n2 - Typing Speed Text\n3 - Tetris\n>>> ")
        if game == "1":
            os.system("python tictactoe.py")
            subprocess.run(["python", "tictactoe.py"])

        if game == "2":
            os.system("python speed_typing.py")
            subprocess.run(["python", "speed_typing.py"])
        
        if game == "3":
            os.system("python Py_Game.py")
            subprocess.run(["python", "Py_Game.py"])
