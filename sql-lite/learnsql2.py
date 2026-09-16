import sqlite3

conn = sqlite3.connect("test.db")

cur = conn.cursor()


cur.execute("""
    CREATE TABLE IF NOT EXISTS clips (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

cur.execute("INSERT INTO clips (content) VALUES (?)", ("hello my first clip",))
conn.commit()

print(cur.fetchone())



conn.close()