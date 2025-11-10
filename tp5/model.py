# model.py
import sqlite3
import re

class UserModel:
    def __init__(self, db_name="users.db"):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')
        conn.commit()
        conn.close()

    def validate_user(self, username, password):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT 1 FROM users WHERE username=? AND password=?", (username, password))
        result = c.fetchone()
        conn.close()
        return result is not None

    def add_user(self, username, password):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    @staticmethod
    def is_valid_password(password):
        
        return len(password) >= 6 and re.search(r'\d', password)