import tkinter as tk
from tkinter import messagebox


class LoginView:
    """
    Main login window using the grid layout manager.
    """

    def __init__(self, controller):
        self.controller = controller

        # Main window
        self.root = tk.Tk()
        self.root.title("Login System (MVC + Grid)")
        self.root.geometry("350x170")

        # Configure grid columns
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

       
        tk.Label(self.root, text="Username:").grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )

        self.username_entry = tk.Entry(self.root, width=30)
        self.username_entry.grid(
            row=0, column=1, padx=10, pady=10, sticky="e"
        )

    
        tk.Label(self.root, text="Password:").grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )

        self.password_entry = tk.Entry(self.root, show="*", width=30)
        self.password_entry.grid(
            row=1, column=1, padx=10, pady=10, sticky="e"
        )

        
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        tk.Button(
            button_frame,
            text="Login",
            command=self.controller.handle_login
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            button_frame,
            text="Register",
            command=self.controller.handle_register
        ).pack(side=tk.LEFT, padx=5)

      
        self.message_label = tk.Label(self.root, text="", fg="blue")
        self.message_label.grid(row=3, column=0, columnspan=2, pady=5)

    # 
    def get_credentials(self):
        """Return username and password."""
        return self.username_entry.get(), self.password_entry.get()

    # 
    def show_message(self, message, color="blue"):
        """Display login status message."""
        self.message_label.config(text=message, fg=color)

    # 
    def main_loop(self):
        self.root.mainloop()



class RegistrationView:
    """
    Registration window using Tkinter Toplevel.
    """

    def __init__(self, parent, controller):
        self.controller = controller

        # Toplevel window
        self.window = tk.Toplevel(parent)
        self.window.title("Register New User")
        self.window.geometry("400x230")

        # Configure grid
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)

        tk.Label(self.window, text="Username:").grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )

        self.username_entry = tk.Entry(self.window, width=30)
        self.username_entry.grid(
            row=0, column=1, padx=10, pady=10, sticky="e"
        )

       
        tk.Label(self.window, text="Password:").grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )

        self.password_entry = tk.Entry(self.window, show="*", width=30)
        self.password_entry.grid(
            row=1, column=1, padx=10, pady=10, sticky="e"
        )

       
        tk.Label(self.window, text="Confirm Password:").grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )

        self.confirm_password_entry = tk.Entry(self.window, show="*", width=30)
        self.confirm_password_entry.grid(
            row=2, column=1, padx=10, pady=10, sticky="e"
        )

        
        tk.Button(
            self.window,
            text="Submit",
            command=self.controller.handle_submit_registration
        ).grid(row=3, column=0, columnspan=2, pady=15)

        
        self.message_label = tk.Label(self.window, text="", fg="blue")
        self.message_label.grid(row=4, column=0, columnspan=2, pady=5)

        # Make window modal
        self.window.transient(parent)
        self.window.grab_set()

    
    def get_credentials(self):
        """Return username, password, and confirm password."""
        return (
            self.username_entry.get(),
            self.password_entry.get(),
            self.confirm_password_entry.get()
        )

    # ----------------------------------------------------------------
    def show_message(self, message, color="blue"):
        """Display registration status message."""
        self.message_label.config(text=message, fg=color)

    # ----------------------------------------------------------------
    def close(self):
        self.window.destroy()
