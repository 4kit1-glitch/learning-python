import sqlite3
# this script shows using an sqllite 

conn = sqlite3.connect("employee.db")

cur = conn.cursor()

cur.execute("SELECT * FROM employees")
print(cur.fetchone())