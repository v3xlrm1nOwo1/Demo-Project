import threading
import sqlite3
import socket
import re

# ====================================================================================================================== #
# address "192.168.56.1"
HOST =  socket.gethostname() # localhost
# print(HOST)
PORT = 1234
address = (HOST, PORT)

# ====================================================================================================================== #
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen()

# ====================================================================================================================== #

# Created DB
con = sqlite3.connect("Demo.db", check_same_thread=False)
cur = con.cursor()
# cur.execute("CREATE TABLE info(ID INTEGER PRIMARY KEY AUTOINCREMENT, username UNIQUE, email, password)")
# ====================================================================================================================== #
# Function For Add User
def add_user(data):
    cur.executemany("INSERT INTO info(username, email, password) VALUES(?, ?, ?)", data)
    con.commit()

# ====================================================================================================================== #
# Function For Search User
def search(_username):
    for row in cur.execute(f"SELECT * FROM info WHERE username = '{_username}'"):
        return row

# ====================================================================================================================== #
# Function For Send Msg
def send(msg):
    return str(msg).rjust(1024, " ").encode("utf-8")

# ====================================================================================================================== #
# Function For Recv Msg
def recv(conn):
    conn.recv(1024).decode("utf-8").strip()

# ====================================================================================================================== #
# Function For Delete User
def _search(email, password):
    for row in cur.execute(f"SELECT * FROM info WHERE email = '{email}' AND password = '{password}'"):
        return row
# ====================================================================================================================== #
l1 = []
l2 = []
username = "" 
def acount(conn):
    conn.sendall(send("signup or login"))
    opration = recv(conn)
    print(f">>> {opration}")

    if opration == "signup":

        # Name
        while True:
            conn.sendall(send("name"))
            name = recv(conn)
            if name.isalpha():
                l1.append(name)
                break

        
        # Email
        while True:
            conn.sendall(send("email"))
            email = recv(conn)
            if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
                l1.append(email)
                break

        #password
        while True:
            conn.sendall(send("password"))
            password = recv(conn)
            l, u, p, d = 0, 0, 0, 0
            if (len(password) >= 8): #"R@m@_f0rtu9e$"
                for i in password:

                    # counting lowercase alphabets
                    if (i.islower()):
                        l+=1		

                    # counting uppercase alphabets
                    if (i.isupper()):
                        u+=1		

                    # counting digits
                    if (i.isdigit()):
                        d+=1		

                    # counting the mentioned special characters
                    if(i=='@'or i=='$' or i=='_'):
                        p+=1		
            if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
                print("Valid Password")
                l1.append(password)
                print(l1)
                if len(l1) == 3:
                    print(l1)
                    data = [(l1[0], l1[1], l1[2])]
                    print(search(l1[0]))
                    if not search(l1[0]):
                        add_user(data)
                        username = name
                        print(f"Create user, username is: {username}")
                        return username
                        break
                        
                    else:
                        print("user in DB")

                        break
            else:
                print("Invalid Password")
    
    # Login
    elif opration == "login":
        # Email
        while True:
            conn.sendall(send("email"))
            email = recv(conn)
            if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
                l2.append(email)
                break

        #password
        while True:
            conn.sendall(send("password"))
            password = recv(conn)
            l, u, p, d = 0, 0, 0, 0
            if (len(password) >= 8): #"R@m@_f0rtu9e$"
                for i in password:

                    # counting lowercase alphabets
                    if (i.islower()):
                        l+=1		

                    # counting uppercase alphabets
                    if (i.isupper()):
                        u+=1		

                    # counting digits
                    if (i.isdigit()):
                        d+=1		

                    # counting the mentioned special characters
                    if(i=='@'or i=='$' or i=='_'):
                        p+=1		
            if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
                print("Valid Password")
                l2.append(password)
                if len(l2) == 2:
                    print(l2)
                    if _search(email, password):
                        username = _search(email, password)[1]
                        print(f"you can login, username is: {username}")
                        return username
                        
                break
            else:
                print("Invalid Password")

    else:
        conn.sendall(send("wtf"))
# ====================================================================================================================== #

def main():
    print(">>> Start <<<")
    while True:
        conn, addr = server.accept()
        print(f"Connction from  ({addr}) has been established!!!")
        user = acount(conn=conn)
        if user:
            conn.sendall(send("select game"))
        else:
            user = acount(conn=conn)


           
thread = threading.Thread(target=main)
thread.start()

# add_user_thread = threading.Thread(target=add_user)
# add_user_thread.start()   

# search_thread = threading.Thread(target=main)
# search_thread.start()
