import threading
import socket
import sqlite3

# address
HOST = socket.gethostname() # localhost
PORT = 1234
address = (HOST, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)



def send(data):
    return str(data).rjust(1024, " ").encode("utf-8")
msg = client.recv(1024)
msg = msg.decode("utf-8").strip()
print(msg)
if msg == "True":
    print(msg)
    print(">>> you can:\n1 - add.\n2 - search.\n3 - delete.")
    oprations = input("Enter Oprations or enter logout to end conn: ")
    oprations = oprations.lower()
    print(oprations)
    client.sendall(send(oprations))
    # if oprations == "logout":
    #     pass
    # print("=" * 50)

while True:
    
    if oprations == "add":
        messg = client.recv(1024).decode("utf-8").strip()
            
            # frist name
        if messg == "frist_name":
            frisrt_name = input(">>> Enter You Frist Name: ")
            client.sendall(send(frisrt_name.lower()))
            
            # last name
        elif messg == "last_name":
            last_name = input(">>> Enter You Last Name: ")
            client.sendall(send(last_name))
                
            # address
        elif messg == "address":
            print(client.recv(1024).decode("utf-8").strip())
            address = input(">>> Enter You address: ")
            client.sendall(send(address.upper()))
        
        elif messg == "academic":
            academic = input(">>> Enter You academic: ")
            client.sendall(send(academic.lower()))
        
        elif messg == "year":
            year = input(">>> Enter You year: ")
            client.sendall(send(year))
        
        elif messg == "semester":
            semester = input(">>> Enter You semester: ")
            client.sendall(send(semester))
        
        elif messg == "tel":
            tel = input(">>> Enter You tel: ")
            client.sendall(send(tel))
            print("=" * 50)

        # elif messg == "opr":
        #     print(">>> you can:\n1 - add.\n2 - search.\n3 - delete.")
        #     oprations = input("Enter Oprations or enter logout to end conn: ")
        #     if oprations == "logout":
        #         client.sendall(send(oprations))

        else:
            print(f"{messg}") 
            print("=" * 50)
            break
        

            # print(">>> you can:\n1 - add.\n2 - search.\n3 - delete.")
            # oprations = input("Enter Oprations or enter logout to end conn: ")
            # if oprations == "logout":
            #     client.sendall(send(oprations))


        
            
            
    elif oprations == "search":
        id = input("Enter your ID: ")
        client.sendall(send(id))
        print(client.recv(1024).decode("utf-8").strip())
        print("=" * 50)
        break
        # print(">>> you can:\n1 - add.\n2 - search.\n3 - delete.")
        # oprations = input("Enter Oprations or enter logout to end conn: ")
        # if oprations == "logout":
        #     client.sendall(send(oprations))
    
    elif oprations == "delete":
        id = input("Enter your ID: ")
        client.sendall(send(id))
        print(client.recv(1024).decode("utf-8").strip())
        print("=" * 50)
        break
        # print(">>> you can:\n1 - add.\n2 - search.\n3 - delete.")
        # oprations = input("Enter Oprations or enter logout to end conn: ")
        # if oprations == "logout":
        #     client.sendall(send(oprations))


    elif oprations == "logout":
        client.sendall(send("logout"))
        client.close()
        break
        print("=" * 50)

    else:
        print("=" * 50)
        break

# thread = threading.Thread(target=main)
# thread.start()
