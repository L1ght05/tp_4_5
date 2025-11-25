# controller.py 
from model import UserModel
from view import LoginView


class LoginController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView(self)

    def handle_login(self):
        username, password = self.view.get_login_credentials()

        if not username or not password:
            self.view.show_login_message("⚠️ Please enter both fields.", "orange")
            return

        if self.model.validate_user(username, password):
            self.view.show_login_message(f"✅ Welcome, {username}!", "green")
        else:
            self.view.show_login_message("❌ Invalid username or password", "red")

    def handle_register(self):
        self.view.show_register()
        self.view.clear_register_fields()

    def handle_back_to_login(self):
        self.view.show_login()
        self.view.clear_login_fields()

    def handle_submit_registration(self):
        username, password, confirm = self.view.get_register_credentials()

        # 1. Required fields
        if not username or not password or not confirm:
            self.view.show_register_message("⚠️ All fields are required.", "red")
            return

        # 2. Password match
        if password != confirm:
            self.view.show_register_message("⚠️ Passwords do not match.", "red")
            return

        # 3.  ENFORCE PASSWORD POLICY (≥6 chars + 1 digit)
        if not self.model.is_valid_password(password):
            self.view.show_register_message(
                "⚠️ Password must be ≥6 characters and include at least 1 digit.",
                "red"
            )
            return

        # 4. Add user
        if self.model.add_user(username, password):
            self.view.show_register_message("✅ Registration successful!", "green")
            self.view.root.after(1200, self.handle_back_to_login)
        else:
            self.view.show_register_message("⚠️ Username already exists.", "red")

    def run(self):
        self.view.main_loop()