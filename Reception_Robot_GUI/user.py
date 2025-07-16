from PyQt6.QtWidgets import QMessageBox
from ui.style import QMSGBOX_STYLE

def handle_login(ui, registered_users):
    username = ui.Signin_username.text()
    password = ui.Signin_password.text()

    for user in registered_users:
        if user["username"] == username and user["password"] == password:
            return True  # Thành công
    msg = QMessageBox()
    msg.setWindowTitle("Login Failed")
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setText("Incorrect username or password")
    msg.setStyleSheet(QMSGBOX_STYLE)
    msg.exec()
    return False

def handle_signup(ui, registered_users):
    fullname = ui.Signup_name.text()
    phone    = ui.Signup_phone.text()
    username = ui.Signup_username.text()
    password = ui.Signup_password.text()
    verify   = ui.Signup_code.text()

    if not all([fullname, phone, username, password, verify]):
        msg = QMessageBox()
        msg.setWindowTitle("Sign Up Failed")
        msg.setText("Please fill in all fields")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStyleSheet(QMSGBOX_STYLE)
        msg.exec()
        return False

    if verify.strip().lower() != "fablab":
        msg = QMessageBox()
        msg.setWindowTitle("Sign Up Failed")
        msg.setText("Incorrect verification code")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStyleSheet(QMSGBOX_STYLE)
        msg.exec()
        return False

    for user in registered_users:
        if user["username"] == username:
            msg = QMessageBox()
            msg.setWindowTitle("Sign Up Failed")
            msg.setText("Username already exists")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStyleSheet(QMSGBOX_STYLE)
            msg.exec()
            return False

    registered_users.append({
        "fullname": fullname,
        "phone": phone,
        "username": username,
        "password": password,
        "verify": verify
    })
    msg = QMessageBox()
    msg.setWindowTitle("Success")
    msg.setText("Account created successfully")
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setStyleSheet(QMSGBOX_STYLE)
    msg.exec()  
    return True


def handle_logout(main_window):
    reply = QMessageBox.question(
        main_window,
        "Confirm Logout",
        "Are you sure you want to log out?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    )
    if reply == QMessageBox.StandardButton.Yes:
        main_window._shutdown_all_services()
        main_window.ui.Page.setCurrentWidget(main_window.ui.Page_signin)
        main_window.ui.Dashboard.setCurrentWidget(main_window.ui.Dashboard_signin)
