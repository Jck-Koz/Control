import bcrypt
import keyring
from keyring.errors import PasswordDeleteError
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from .login_ui import Ui_Windowlogin
from database.database import create_connection, close_connection
from base_window.base_window import BaseWindow
import traceback


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        print("Initializing LoginWindow...")
        self.ui = Ui_Windowlogin()
        self.ui.setupUi(self)
        self.ui.Iniciarsesion.clicked.connect(self.login)
        self.db_connection = create_connection()
        print("Database connection created.")

        # Cargar credenciales almacenadas si existen
        self.load_credentials()

    def load_credentials(self):
        try:
            print("Loading stored credentials...")
            username = keyring.get_password('my_app', 'username')
            password = keyring.get_password('my_app', 'password')
            if username and password:
                self.ui.lineEditusername.setText(username)
                self.ui.lineEditpass.setText(password)
                self.ui.rememberMe.setChecked(True)
                print("Credentials loaded.")
        except Exception as e:
            print("Error al cargar las credenciales:", e)
            traceback.print_exc()

    def login(self):
        try:
            username = self.ui.lineEditusername.text()
            password = self.ui.lineEditpass.text()
            print(f"Attempting to login with username: {username}")

            cursor = self.db_connection.cursor()
            cursor.execute(
                "SELECT id_usuario, contraseña, id_rol FROM usuarios WHERE nombre_usuario=%s", (username,))
            user = cursor.fetchone()
            print("User fetched from database:", user)

            if user:
                user_id, hashed_password, role_id = user
                if bcrypt.checkpw(password.encode(), hashed_password.encode()):
                    print("Password match. Redirecting user...")
                    self.remember_credentials(username, password)
                    self.redirect_user(role_id, user_id)
                else:
                    print("Password mismatch.")
                    QMessageBox.warning(
                        self, "Error", "Nombre de usuario o contraseña incorrectos")
            else:
                print("User not found.")
                QMessageBox.warning(
                    self, "Error", "Nombre de usuario o contraseña incorrectos")
        except Exception as e:
            print("Error en el proceso de inicio de sesión:", e)
            traceback.print_exc()

    def remember_credentials(self, username, password):
        try:
            if self.ui.rememberMe.isChecked():
                keyring.set_password('my_app', 'username', username)
                keyring.set_password('my_app', 'password', password)
                print("Credentials remembered.")
            else:
                try:
                    keyring.delete_password('my_app', 'username')
                except PasswordDeleteError:
                    pass
                try:
                    keyring.delete_password('my_app', 'password')
                except PasswordDeleteError:
                    pass
                print("Credentials not remembered.")
        except Exception as e:
            print("Error al guardar las credenciales:", e)
            traceback.print_exc()

    def redirect_user(self, role_id, user_id):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(
                "SELECT nombre_rol FROM roles WHERE id_rol=%s", (role_id,))
            role = cursor.fetchone()[0]
            print(f"Redirecting user with role: {role}")

            self.main_window = BaseWindow(role_id, user_id)
            self.main_window.show()
            print("Main window should now be visible.")
            self.close()
        except Exception as e:
            print("Error al redirigir al usuario:", e)
            traceback.print_exc()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.login()

    def closeEvent(self, event):
        try:
            close_connection(self.db_connection)
            print("Database connection closed.")
        except Exception as e:
            print("Error al cerrar la conexión de la base de datos:", e)
            traceback.print_exc()
        event.accept()
