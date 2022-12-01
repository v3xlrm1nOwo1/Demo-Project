import sqlite3

con = sqlite3.connect("tutorial.db")

cur = con.cursor()

con = sqlite3.connect("Demo.db")
cur = con.cursor()
cur.execute("CREATE TABLE info(first_name, last_name, addr, academic year,semester,Tel)")

