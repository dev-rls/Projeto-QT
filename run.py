from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QStackedWidget, QMessageBox
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'modulos'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'templates'))

from main import LoginDialog, Inicio, TelaPrincipalRegistro, Home

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

