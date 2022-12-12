import threading
import socket
import sqlite3

# address "192.168.56.1"
HOST =  socket.gethostname() # localhost
# print(HOST)
PORT = 1234
address = (HOST, PORT)
id = 1


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen()


# Created DB
con = sqlite3.connect("Demo.db")
cur = con.cursor()
# cur.execute("CREATE TABLE info(ID INTEGER PRIMARY KEY AUTOINCREMENT, first_name, last_name, addr, academic, year,semester,Tel)")


def add_(data_):
    cur.executemany("INSERT INTO info(first_name, last_name, addr, academic, year,semester,Tel) VALUES(?, ?, ?, ?, ?, ?, ?)", data_)
    con.commit()


def searching(ID):
    for row in cur.execute(f"SELECT ID, first_name, last_name, addr, academic, year,semester,Tel FROM info WHERE ID = {ID}"):
        return row


def delete(ID):
    cur.execute(f"DELETE FROM info WHERE ID = {ID}")


def send(msg):
    return str(msg).rjust(1024, " ").encode("utf-8")


def main():
    # print(HOST)

    print("Start.....")
    while True:
        conn, addr = server.accept()
        
        print(f"Connction from  ({addr}) has been established!!!")

        l = []
        
        # send True to client for enter opration or logout
        conn.sendall(send("True"))
               
        # recv opration
        opration = conn.recv(1024).decode("utf-8").strip()
        
        
        if opration == "add":
            print("add")
            while True:
                # Frist Name
                conn.sendall(send("frist_name"))
                frist_name = conn.recv(1024).decode("utf-8").strip()
                if frist_name.isalpha():
                    print(f"Frist name  is valid: {frist_name}")
                    l.append(frist_name)
                    print(l)
                    break
            
            while True:    
                # Last Name
                conn.sendall(send("last_name"))
                last_name = conn.recv(1024).decode("utf-8").strip()
                if last_name.isalpha():
                    print(f"Last name  is valid: {last_name}")
                    l.append(last_name)
                    print(l)
                    break
            
                    
            while True:        
                # Address
                conn.sendall(send("address"))
                conn.sendall(send("You Can only choice: {A - B - C}"))
                address = conn.recv(1024).decode("utf-8").strip()
                if address in ("A", "B", "C"):
                    print(f"Address  is valid: {address}")
                    l.append(address)
                    print(l)
                    break
            
            while True:    
                # Academic
                conn.sendall(send("academic"))
                academic = conn.recv(1024).decode("utf-8").strip()
                if academic.isalpha():
                    print(f"Academic  is valid: {academic}")
                    l.append(academic)
                    print(l)
                    break  
                
            while True:    
                # Year
                conn.sendall(send("year"))
                year = conn.recv(1024).decode("utf-8").strip()
                if year.isdigit():
                    year = int(year)
                    print(f"Year  is valid: {year}")
                    l.append(year)
                    print(l)
                    break      
            
            while True:    
                # Semester
                conn.sendall(send("semester"))
                semester = conn.recv(1024).decode("utf-8").strip()
                if semester.isdigit():
                    semester = int(semester)
                    print(f"Semester  is valid: {semester}")
                    l.append(semester)
                    print(l)
                    break 
            
            
            while True:    
                # Tel
                conn.sendall(send("tel"))
                tel = conn.recv(1024).decode("utf-8").strip()
                if tel.isdigit():
                    print(f"Tel  is valid: {tel}")
                    l.append(tel)
                    print(l)
                    break 
            
            if len(l) == 7:
                l = [(l[0], l[1], l[2], l[3], l[4], l[5], l[6])]
                add_(l)
                for row in cur.execute(f"SELECT ID, first_name, last_name, addr, academic, year,semester,Tel FROM info ORDER BY ID DESC LIMIT 1"):
                    print(row)
                user = f">>> ID: {row[0]}\n>>> First Name: {row[1]}\n>>> Last Name: {row[2]}\n>>> Address: {row[3]}\n>>> Academic: {row[4]}\n>>> Year: {row[5]}\n>>> Semester: {row[6]}\n>>> Tel: {row[7]}"
                conn.sendall(send(user))
                print(f"client info: {user}")
                # conn.sendall(send("opr"))


            
            
                       
            
        elif opration == "search":
            print(opration)
            send("id")
            while True:
                client_id = conn.recv(1024).decode("utf-8").strip()
                if client_id.isdigit():
                    client_id = int(client_id)
                    if searching(client_id):
                        client_info = searching(client_id)
                        user = f">>> ID: {client_info[0]}\n>>> First Name: {client_info[1]}\n>>> Last Name: {client_info[2]}\n>>> Address: {client_info[3]}\n>>> Academic: {client_info[4]}\n>>> Year: {client_info[5]}\n>>> Semester: {client_info[6]}\n>>> Tel: {client_info[7]}"
                        print(user)
                        conn.sendall(send(user))
                    else:
                        conn.sendall(send("Client not found!!!!"))
                    break

        
                
        elif opration == "delete":
            print(opration)
            send("id")
            while True:
                client_id = conn.recv(1024).decode("utf-8").strip()
                if client_id.isdigit():
                    client_id = int(client_id)
                    if searching(client_id):
                        client_info = searching(client_id)
                        user = f"Deleted this user: \n>>> ID: {client_info[0]}\n>>> First Name: {client_info[1]}\n>>> Last Name: {client_info[2]}\n>>> Address: {client_info[3]}\n>>> Academic: {client_info[4]}\n>>> Year: {client_info[5]}\n>>> Semester: {client_info[6]}\n>>> Tel: {client_info[7]}"
                        print(user)
                        conn.sendall(send(user))
                        client_info = delete(client_id)
                        print(f"delete: {client_info}")
                        break
                    else:
                        conn.sendall(send("Client not found!!!!"))
                        break
                
                
            
        elif opration == "logout":
            conn.close()
            break
            
        else:
            conn.sendall(send("Error ):"))
            break
            

            
thread = threading.Thread(target=main)
thread.start()
                   
main()    
