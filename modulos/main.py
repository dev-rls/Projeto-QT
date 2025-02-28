
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QStackedWidget, QMessageBox
import sys

from templates.Login import Ui_Login  # Certifique-se de que o nome do arquivo e da classe estejam corretos
from templates.Registro import Ui_tela_principal_registro  # Certifique-se de que o nome do arquivo e da classe estejam corretos
from templates.Inicio import Ui_Inicio  # Certifique-se de que o nome do arquivo e da classe estejam corretos
from templates.Home import Ui_Home  # Certifique-se de que o nome do arquivo e da classe estejam corretos

class Inicio(QDialog):
    def __init__(self, stacked_widget):
        super().__init__()
        self.ui = Ui_Inicio()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.btn_login.clicked.connect(self.go_to_login)
        self.ui.btn_criarConta.clicked.connect(self.go_to_register)

    def go_to_login(self):
        self.stacked_widget.setCurrentIndex(1)  # Alterar para o índice da tela de Login

    def go_to_register(self):
        self.stacked_widget.setCurrentIndex(2)  # Alterar para o índice da tela de Registro

class LoginDialog(QDialog):
    def __init__(self, stacked_widget):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.btn_entrar.clicked.connect(self.check_login)

    def check_login(self):
        username = self.ui.input_user.text()
        password = self.ui.input_senha.text()

        if username == "admin" and password == "admin":
            self.stacked_widget.setCurrentIndex(3)  # Alterar para o índice da tela de Home
        else:
            QMessageBox.warning(self, "Erro de Login", "Usuário ou senha incorretos. Tente novamente.")

class TelaPrincipalRegistro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_tela_principal_registro()
        self.ui.setupUi(self)
        self.ui.btn_registrar.clicked.connect(self.register_user)

    def register_user(self):
        # Lógica de registro do usuário (você pode adicionar a sua própria lógica aqui)
        QMessageBox.information(self, "Registrado", "Registrado com sucesso!")

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Home()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    stacked_widget = QStackedWidget()
    inicio = Inicio(stacked_widget)
    login = LoginDialog(stacked_widget)
    register = TelaPrincipalRegistro()
    home = Home()

    stacked_widget.addWidget(inicio)  # Índice 0
    stacked_widget.addWidget(login)   # Índice 1
    stacked_widget.addWidget(register) # Índice 2
    stacked_widget.addWidget(home)    # Índice 3

    stacked_widget.setCurrentIndex(0)  # Mostra a tela de Início inicialmente
    stacked_widget.show()

    sys.exit(app.exec())



