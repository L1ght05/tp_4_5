import tkinter as tk
import sqlite3
import re

# DATABASE (Model)
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def validate_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT 1 FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None

def add_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# CONTROLLER LOGIC
def is_valid_password(pwd):
    return len(pwd) >= 6 and re.search(r'\d', pwd)

# VIEW + APP

class App:
    def __init__(self):
        init_db()
        self.login_window = tk.Tk()
        self.login_window.title("Login System")
        self.login_window.geometry("300x260")
        self.welcome_win = None

        tk.Label(self.login_window, text="Username:").pack(pady=5)
        self.user_entry = tk.Entry(self.login_window)
        self.user_entry.pack()

        tk.Label(self.login_window, text="Password:").pack(pady=5)
        self.pass_entry = tk.Entry(self.login_window, show="*")
        self.pass_entry.pack()

        self.show_pass_var = tk.BooleanVar()
        tk.Checkbutton(
            self.login_window,
            text="Show Password",
            variable=self.show_pass_var,
            command=self.toggle_password
        ).pack()

        tk.Button(self.login_window, text="Login", command=self.login).pack(pady=8)
        tk.Button(self.login_window, text="Register", command=self.register).pack()
        self.msg_label = tk.Label(self.login_window, text="", fg="blue")
        self.msg_label.pack(pady=10)

    def toggle_password(self):
        self.pass_entry.config(show="" if self.show_pass_var.get() else "*")

    def show_message(self, text, color):
        self.msg_label.config(text=text, fg=color)

    def clear_form(self):
        self.user_entry.delete(0, tk.END)
        self.pass_entry.delete(0, tk.END)
        self.show_pass_var.set(False)
        self.toggle_password()
        self.show_message("", "blue")

    def login(self):
        user = self.user_entry.get()
        pwd = self.pass_entry.get()
        if not user or not pwd:
            self.show_message("Enter both fields", "orange")
            return
        if validate_user(user, pwd):
            self.login_window.withdraw()
            self.open_welcome(user)
        else:
            self.show_message("Invalid username or password", "red")

    def register(self):
        user = self.user_entry.get()
        pwd = self.pass_entry.get()
        if not user or not pwd:
            self.show_message("Enter both fields", "orange")
        elif not is_valid_password(pwd):
            self.show_message("Password: ≥6 chars + 1 digit", "orange")
        elif add_user(user, pwd):
            self.show_message("Registered successfully!", "green")
        else:
            self.show_message("Username already exists", "red")

    def open_welcome(self, username):
        self.welcome_win = tk.Toplevel()
        self.welcome_win.title("Welcome")
        self.welcome_win.geometry("300x150")
        self.welcome_win.protocol("WM_DELETE_WINDOW", self.logout)

        tk.Label(self.welcome_win, text=f"Welcome, {username}!", font=("Arial", 14)).pack(pady=30)
        tk.Button(self.welcome_win, text="Logout", command=self.logout).pack()

    def logout(self):
        if self.welcome_win:
            self.welcome_win.destroy()
            self.welcome_win = None
        self.login_window.deiconify()
        self.clear_form()

    def run(self):
        self.login_window.mainloop()
if __name__ == "__main__":
    App().run()