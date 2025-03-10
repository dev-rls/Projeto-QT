from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QStackedWidget, QMessageBox
from PySide6.QtCore import QSize
import sys

from templates.Login import Ui_Login
from templates.Registro import Ui_tela_principal_registro
from templates.Inicio import Ui_Inicio
from templates.Home import Ui_Home

class Inicio(QDialog):
    def __init__(self, stacked_widget):
        super().__init__()
        self.ui = Ui_Inicio()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.btn_login.clicked.connect(self.go_to_login)
        self.ui.btn_criarConta.clicked.connect(self.go_to_register)

    def preferred_size(self):
        return QSize(870, 455)  # Tamanho desejado para a tela de início

    def go_to_login(self):
        self.stacked_widget.resize(self.stacked_widget.widget(1).preferred_size())  # Redimensiona para o tamanho do Login
        self.stacked_widget.setCurrentIndex(1)

    def go_to_register(self):
        self.stacked_widget.resize(self.stacked_widget.widget(2).preferred_size())  # Redimensiona para o tamanho do Registro
        self.stacked_widget.setCurrentIndex(2)

class LoginDialog(QDialog):
    def __init__(self, stacked_widget):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.btn_entrar.clicked.connect(self.check_login)

    def preferred_size(self):
        return QSize(890, 505)  # Tamanho desejado para a tela de login (exemplo)

    def check_login(self):
        username = self.ui.input_user.text()
        password = self.ui.input_senha.text()
        if username == "admin" and password == "admin":
            self.stacked_widget.resize(self.stacked_widget.widget(3).preferred_size())  # Redimensiona para o tamanho do Home
            self.stacked_widget.setCurrentIndex(3)
        else:
            QMessageBox.warning(self, "Erro de Login", "Usuário ou senha incorretos.")

class TelaPrincipalRegistro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_tela_principal_registro()
        self.ui.setupUi(self)
        self.ui.btn_registrar.clicked.connect(self.register_user)

    def preferred_size(self):
        return QSize(887, 505)  # Tamanho desejado para a tela de registro (exemplo)

    def register_user(self):
        QMessageBox.information(self, "Registrado", "Registrado com sucesso!")

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Home()
        self.ui.setupUi(self)

    def preferred_size(self):
        return QSize(848, 500)  # Tamanho desejado para a tela de home (exemplo)