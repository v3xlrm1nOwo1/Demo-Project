# import sqlite3

# con = sqlite3.connect("Demo.db")
# cur = con.cursor()
# # cur.execute("CREATE TABLE infoh(ID, first_name, last_name, addr, academic, year,semester,Tel)")
# #

# def add_(data):
#     cur.executemany("INSERT INTO infoh VALUES(?, ?, ?, ?, ?, ?, ?, ?)", data)
#     con.commit()


# def searching(id):
#     for row in cur.execute(f"SELECT ID, first_name, last_name, addr, academic, year,semester,Tel FROM infoh WHERE ID = {id}"):
#         print(row)


# data = [
#     (1,'batool','gammer','bahry','nw',2022,6,'0927490519')
# ]

# add_(data)

# searching(1)
list_ = [1, 2, 3, 4, 5, 6, 7, 8]
l = (list_[0], list_[1], list_[2], list_[3], list_[4], list_[5], list_[6], list_[7])
list_ = [l]
print(list_)
