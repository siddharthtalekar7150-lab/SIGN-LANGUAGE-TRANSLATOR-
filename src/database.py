# database.py - Save custom signs
import sqlite3


class SignDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('vit_signs.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS customs 
                            (id INTEGER PRIMARY KEY, name TEXT, meaning TEXT)''')

    def add_sign(self, name, meaning):
        self.conn.execute("INSERT INTO customs (name, meaning) VALUES (?, ?)", (name, meaning))
        self.conn.commit()
        print(f"Added: {name} = {meaning}")

    def show_all(self):
        cursor = self.conn.execute("SELECT * FROM customs")
        for row in cursor:
            print(f"{row[1]} → {row[2]}")
