from PySide6.QtWidgets import QMessageBox

def handle_login(ui, registered_users):
    username = ui.Signin_username.text()
    password = ui.Signin_password.text()

    for user in registered_users:
        if user["username"] == username and user["password"] == password:
            return True  # Thành công
    QMessageBox.warning(None, "Login Failed", "Incorrect username or password")
    return False

def handle_signup(ui, registered_users):
    fullname = ui.Signup_name.text()
    phone    = ui.Signup_phone.text()
    username = ui.Signup_username.text()
    password = ui.Signup_password.text()
    verify   = ui.Signup_code.text()

    if not all([fullname, phone, username, password, verify]):
        QMessageBox.warning(None, "Sign Up Failed", "Please fill in all fields.")
        return False

    if verify.strip().lower() != "fablab":
        QMessageBox.warning(None, "Sign Up Failed", "Incorrect verification code.")
        return False

    for user in registered_users:
        if user["username"] == username:
            QMessageBox.warning(None, "Sign Up Failed", "Username already exists.")
            return False

    registered_users.append({
        "fullname": fullname,
        "phone": phone,
        "username": username,
        "password": password,
        "verify": verify
    })

    QMessageBox.information(None, "Success", "Account created successfully!")
    return True


def handle_logout(main_window):
    reply = QMessageBox.question(
        main_window,
        "Confirm Logout",
        "Are you sure you want to log out?",
        QMessageBox.Yes | QMessageBox.No
    )
    if reply == QMessageBox.Yes:
        main_window._shutdown_all_services()
        main_window.ui.Page.setCurrentWidget(main_window.ui.Page_signin)
        main_window.ui.Dashboard.setCurrentWidget(main_window.ui.Dashboard_signin)
