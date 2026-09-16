import sqlite3

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        first TEXT NOT NULL,
        last TEXT,
        pay INTEGER, 
        employed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
cur.execute("INSERT INTO employees (first, last, pay) VALUES (:first,:last ,:pay)",{"first":"kengah", "last":"ireneaus", "pay":10000})
conn.commit()

employees = [
    ("nathalia", "bum", 1000),
    ("sintia", "doe" ,10000),
    ("nathalia", "bum", 1000),
    ("sintia", "doe" ,140000),
    ("sintia", "doe" ,30000),
    ("sintia", "doe" ,20),
    ("sintia", "doe" ,1003),
    ("sintia", "doe" ,1),
    ("sintia", "doe" ,100),
    ("sintia", "doe" ,1000),
    ("sintia", "doe" ,100000),
]


cur.executemany("INSERT INTO employees (first, last, pay) VALUES (?, ?, ?)", employees)

conn.commit()
conn.close()