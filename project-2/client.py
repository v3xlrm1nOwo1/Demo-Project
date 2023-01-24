import socket

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

    if msg == "signup or login":
        choice = input(">>> Slect signup or login: ")
        client.sendall(send(choice))

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
        pass
