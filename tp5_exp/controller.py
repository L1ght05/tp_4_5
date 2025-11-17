from model import UserModel
from view import LoginView, RegistrationView


class LoginController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView(self)

        # Holder for the registration window instance
        self.registration_view = None

    # =============================================================
    #                         LOGIN HANDLING
    # =============================================================
    def handle_login(self):
        username, password = self.view.get_credentials()

        if self.model.validate_user(username, password):
            self.view.show_message(f"Welcome, {username}!", "green")
        else:
            self.view.show_message("Invalid username or password", "red")

    # =============================================================
    #                    OPEN REGISTRATION WINDOW
    # =============================================================
    def handle_register(self):
        """
        Open the registration window.
        """
        # If already open, bring it to front instead of creating a new one
        if self.registration_view is not None:
            try:
                self.registration_view.window.lift()
                return
            except:
                # Window was closed manually
                self.registration_view = None

        # Create a new RegistrationView
        self.registration_view = RegistrationView(
            parent=self.view.root,
            controller=self
        )

    # =============================================================
    #                HANDLE "Submit" IN REGISTRATION WINDOW
    # =============================================================
    def handle_submit_registration(self):
        if self.registration_view is None:
            return  # Safety check

        username, password, confirm = self.registration_view.get_credentials()

        # 1. Validation
        if not username or not password or not confirm:
            self.registration_view.show_message(
                "All fields are required.",
                "red"
            )
            return

        if password != confirm:
            self.registration_view.show_message(
                "Passwords do not match.",
                "red"
            )
            return

        # 2. Try adding user
        if self.model.add_user(username, password):
            self.registration_view.show_message(
                "User registered successfully!",
                "green"
            )
            # auto-close after success
            self.registration_view.close()
            self.registration_view = None
        else:
            self.registration_view.show_message(
                "Username already exists.",
                "red"
            )

    # =============================================================
    #                         MAIN LOOP
    # =============================================================
    def run(self):
        self.view.main_loop()
