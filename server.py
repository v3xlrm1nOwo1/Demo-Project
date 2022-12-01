import threading
import socket
import sqlite3

# addr
host = "127.0.0.1" # localhost
port = 1234
id = 1

con = sqlite3.connect("Demo.db")
cur = con.cursor()
cur.execute("CREATE TABLE infoh(ID PRIMARY KEY, first_name, last_name, addr, academic, year,semester,Tel)")



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


def add_(data):
    cur.executemany("INSERT INTO infoh VALUES(?, ?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()


def searching(id):
    for row in cur.execute(f"SELECT ID, first_name, last_name, addr, academic, year,semester,Tel FROM infoh WHERE ID = {id}"):
        print(row)


def send(data):
    return str(data).rjust(1024, " ").encode("utf-8")


def main():
    server.listen()
    conn, addr = server.accept()
    list_ = []
    l = ()
    print("Online.....")
    send("You can add and search")
    
    if dat.decode("utf-8").strip() == "add":
        send("fname")
        if type(dat.decode("utf-8").strip()) == str:
            list_.append(dat.decode("utf-8").strip())
            
            send("lname")
            if type(dat.decode("utf-8").strip()) == str:
                list_.append(dat.decode("utf-8").strip())
                
                l = []
                send(f"you can addr: {l}")
                send("addr")
                if type(dat.decode("utf-8").strip()) == str and dat.decode("utf-8").strip() in l:
                    list_.append(dat.decode("utf-8").strip())
                    
        if len(list_) == 7:
            l = (id, list_[0], list_[1], list_[2], list_[3], list_[4], list_[5], list_[6])
            list_ = [l]
            add_(list_)
            id += 1
                
        else:
            send("try enter your data...")
    
    elif dat.decode("utf-8").strip() == "search":
        send("id")
        if searching(dat.decode("utf-8").strip()):
            send(searching(dat.decode("utf-8").strip()))
        else:
            send("")
    
    
    else:
        send("Error ):")
        
    thread = threading.Thread(target=add_, args=(data, ))
    thread.start()
        
    thread = threading.Thread(target=searching, args=(id, ))
    thread.start()