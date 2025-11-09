# view.py
import tkinter as tk

class LoginView:
    def __init__(self, controller):
        self.controller = controller

        # Login window
        self.root = tk.Tk()
        self.root.title("Login System (MVC Example)")
        self.root.geometry("300x260")

        tk.Label(self.root, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        # Show/Hide checkbox (Exercise 1)
        self.show_password_var = tk.BooleanVar()
        tk.Checkbutton(
            self.root,
            text="Show Password",
            variable=self.show_password_var,
            command=self.toggle_password_visibility
        ).pack()

        tk.Button(self.root, text="Login", command=self.controller.handle_login).pack(pady=8)
        tk.Button(self.root, text="Register", command=self.controller.handle_register).pack()

        self.message_label = tk.Label(self.root, text="", fg="blue")
        self.message_label.pack(pady=10)

        # Welcome window reference
        self.welcome_window = None

    def toggle_password_visibility(self):
        show = "" if self.show_password_var.get() else "*"
        self.password_entry.config(show=show)

    def get_credentials(self):
        return self.username_entry.get().strip(), self.password_entry.get()

    def show_message(self, message, color="blue"):
        self.message_label.config(text=message, fg=color)

    def clear_form(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.show_password_var.set(False)
        self.toggle_password_visibility()
        self.show_message("")

    # ======== NEW: Welcome Window (Exercise 3) ========
    def open_welcome_window(self, username):
        self.welcome_window = tk.Toplevel(self.root)
        self.welcome_window.title("Welcome")
        self.welcome_window.geometry("300x150")
        self.welcome_window.protocol("WM_DELETE_WINDOW", self.controller.on_logout)

        tk.Label(self.welcome_window, text=f"Welcome, {username}!", font=("Arial", 14)).pack(pady=30)
        tk.Button(self.welcome_window, text="Logout", command=self.controller.on_logout).pack()

    def hide_login_window(self):
        self.root.withdraw()

    def show_login_window(self):
        self.root.deiconify()

    def close_welcome_window(self):
        if self.welcome_window:
            self.welcome_window.destroy()
            self.welcome_window = None

    def main_loop(self):
        self.root.mainloop()