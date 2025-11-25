# view.py 
import tkinter as tk


class LoginView:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.title("Login System (MVC + Frame Swap)")
        self.root.geometry("420x340")
        self.root.resizable(False, False)

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.login_frame = self._create_login_frame()
        self.register_frame = self._create_register_frame()

        self.show_login()

    # LOGIN FRAME
    def _create_login_frame(self):
        frame = tk.Frame(self.container, padx=30, pady=30)

        tk.Label(frame, text="🔐 Login", font=("Arial", 16, "bold")).grid(
            row=0, column=0, columnspan=3, pady=(0, 20)
        )

        # Username
        tk.Label(frame, text="Username:").grid(row=1, column=0, sticky="w", pady=8)
        self.username_entry = tk.Entry(frame, width=28)
        self.username_entry.grid(row=1, column=1, columnspan=2, padx=(10, 0), pady=8, sticky="w")

        # Password
        tk.Label(frame, text="Password:").grid(row=2, column=0, sticky="w", pady=8)
        self.password_entry = tk.Entry(frame, show="*", width=25)
        self.password_entry.grid(row=2, column=1, padx=(10, 0), pady=8, sticky="w")

        # Show password toggle
        self.login_show_var = tk.BooleanVar()
        self.login_eye_btn = tk.Button(
            frame,
            text="👁",
            width=3,
            command=self.toggle_login_password
        )
        self.login_eye_btn.grid(row=2, column=2, padx=(5, 0), pady=8, sticky="w")

        # Buttons
        button_frame = tk.Frame(frame)
        button_frame.grid(row=3, column=0, columnspan=3, pady=25)

        tk.Button(button_frame, text="Login", width=10, command=self.controller.handle_login).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Register", width=10, command=self.controller.handle_register).pack(side=tk.LEFT, padx=5)

        # Message
        self.message_label = tk.Label(frame, text="", fg="blue", font=("Arial", 10))
        self.message_label.grid(row=4, column=0, columnspan=3, pady=(10, 0))

        return frame

    
    # REGISTER FRAME
    def _create_register_frame(self):
        frame = tk.Frame(self.container, padx=30, pady=20)

        tk.Label(frame, text="📝 Register", font=("Arial", 16, "bold")).grid(
            row=0, column=0, columnspan=3, pady=(0, 20)
        )

        # Username
        tk.Label(frame, text="Username:").grid(row=1, column=0, sticky="w", pady=8)
        self.reg_username_entry = tk.Entry(frame, width=28)
        self.reg_username_entry.grid(row=1, column=1, columnspan=2, padx=(10, 0), pady=8, sticky="w")

        # Password
        tk.Label(frame, text="Password:").grid(row=2, column=0, sticky="w", pady=8)
        self.reg_password_entry = tk.Entry(frame, show="*", width=25)
        self.reg_password_entry.grid(row=2, column=1, padx=(10, 0), pady=8, sticky="w")

        self.reg_show_var = tk.BooleanVar()
        self.reg_eye_btn1 = tk.Button(
            frame,
            text="👁",
            width=3,
            command=self.toggle_reg_password
        )
        self.reg_eye_btn1.grid(row=2, column=2, padx=(5, 0), pady=8, sticky="w")

        # Confirm Password
        tk.Label(frame, text="Confirm:").grid(row=3, column=0, sticky="w", pady=8)
        self.reg_confirm_entry = tk.Entry(frame, show="*", width=25)
        self.reg_confirm_entry.grid(row=3, column=1, padx=(10, 0), pady=8, sticky="w")

        self.reg_eye_btn2 = tk.Button(
            frame,
            text="👁",
            width=3,
            command=self.toggle_reg_confirm
        )
        self.reg_eye_btn2.grid(row=3, column=2, padx=(5, 0), pady=8, sticky="w")

        # Buttons
        button_frame = tk.Frame(frame)
        button_frame.grid(row=4, column=0, columnspan=3, pady=25)

        tk.Button(button_frame, text="Submit", width=10, command=self.controller.handle_submit_registration).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="← Back", width=10, command=self.controller.handle_back_to_login).pack(side=tk.LEFT, padx=5)

        # Message
        self.reg_message_label = tk.Label(frame, text="", fg="blue", font=("Arial", 10))
        self.reg_message_label.grid(row=5, column=0, columnspan=3, pady=(10, 0))

        return frame

    # PASSWORD TOGGLE METHODS
    def toggle_login_password(self):
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show="")
            self.login_eye_btn.config(text="🙈")
        else:
            self.password_entry.config(show="*")
            self.login_eye_btn.config(text="👁")

    def toggle_reg_password(self):
        if self.reg_password_entry.cget('show') == '*':
            self.reg_password_entry.config(show="")
            self.reg_eye_btn1.config(text="🙈")
        else:
            self.reg_password_entry.config(show="*")
            self.reg_eye_btn1.config(text="👁")

    def toggle_reg_confirm(self):
        if self.reg_confirm_entry.cget('show') == '*':
            self.reg_confirm_entry.config(show="")
            self.reg_eye_btn2.config(text="🙈")
        else:
            self.reg_confirm_entry.config(show="*")
            self.reg_eye_btn2.config(text="👁")

    # PUBLIC INTERFACE
    def show_login(self):
        self.register_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)

    def show_register(self):
        self.login_frame.pack_forget()
        self.register_frame.pack(fill="both", expand=True)

    def get_login_credentials(self):
        return self.username_entry.get(), self.password_entry.get()

    def get_register_credentials(self):
        return (
            self.reg_username_entry.get(),
            self.reg_password_entry.get(),
            self.reg_confirm_entry.get()
        )

    def show_login_message(self, message, color="blue"):
        self.message_label.config(text=message, fg=color)

    def show_register_message(self, message, color="blue"):
        self.reg_message_label.config(text=message, fg=color)

    def clear_login_fields(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.message_label.config(text="")

    def clear_register_fields(self):
        self.reg_username_entry.delete(0, tk.END)
        self.reg_password_entry.delete(0, tk.END)
        self.reg_confirm_entry.delete(0, tk.END)
        self.reg_message_label.config(text="")

    def main_loop(self):
        self.root.mainloop()