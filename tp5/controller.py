# controller.py
from model import UserModel
from view import LoginView

class LoginController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView(self)

    def handle_login(self):
        username, password = self.view.get_credentials()
        if not username or not password:
            self.view.show_message("Enter both username and password", "orange")
            return

        if self.model.validate_user(username, password):
            self.view.hide_login_window()
            self.view.open_welcome_window(username)  # Hint (a): View creates, Controller triggers
        else:
            self.view.show_message("Invalid username or password", "red")

    def handle_register(self):
        username, password = self.view.get_credentials()
        if not username or not password:
            self.view.show_message("Enter both username and password", "orange")
            return

        # Exercise 2: Password validation
        if not self.model.is_valid_password(password):
            self.view.show_message("Password: ≥6 chars + 1 digit", "orange")
            return

        if self.model.add_user(username, password):
            self.view.show_message("User registered successfully!", "green")
            self.view.clear_form()
        else:
            self.view.show_message("Username already exists", "red")

    # ======== NEW: Logout Handler (Exercise 3) ========
    def on_logout(self):
        self.view.close_welcome_window()      # View closes its own window
        self.view.show_login_window()         # Show login again
        self.view.clear_form()                # Reset fields

    def run(self):
        self.view.main_loop()