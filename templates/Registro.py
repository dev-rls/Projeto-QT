# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Registro.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import templates.icones

class Ui_tela_principal_registro(object):
    def setupUi(self, tela_principal_registro):
        if not tela_principal_registro.objectName():
            tela_principal_registro.setObjectName(u"tela_principal_registro")
        tela_principal_registro.resize(900, 509)
        self.tela_registro = QFrame(tela_principal_registro)
        self.tela_registro.setObjectName(u"tela_registro")
        self.tela_registro.setGeometry(QRect(20, 0, 850, 500))
        self.tela_registro.setMaximumSize(QSize(899, 600))
        self.tela_registro.setStyleSheet(u"background-color: rgb(18, 18, 18);")
        self.tela_registro.setFrameShape(QFrame.Shape.StyledPanel)
        self.tela_registro.setFrameShadow(QFrame.Shadow.Raised)
        self.txt_boas_vindas = QLabel(self.tela_registro)
        self.txt_boas_vindas.setObjectName(u"txt_boas_vindas")
        self.txt_boas_vindas.setGeometry(QRect(220, 30, 421, 51))
        self.txt_boas_vindas.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")
        self.btn_registrar = QPushButton(self.tela_registro)
        self.btn_registrar.setObjectName(u"btn_registrar")
        self.btn_registrar.setGeometry(QRect(400, 400, 75, 24))
        self.btn_registrar.setStyleSheet(u"QPushButton {\n"
"	font: 600 9pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(197, 68, 76);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(197, 68, 76);\n"
"}\n"
"")
        self.icon_voltar = QLabel(self.tela_registro)
        self.icon_voltar.setObjectName(u"icon_voltar")
        self.icon_voltar.setGeometry(QRect(30, 30, 26, 26))
        self.icon_voltar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.icon_voltar.setTabletTracking(False)
        self.icon_voltar.setPixmap(QPixmap(u":/icones/icons/voltar_left.png"))
        self.icon_voltar.setScaledContents(True)
        self.icon_fechar = QLabel(self.tela_registro)
        self.icon_fechar.setObjectName(u"icon_fechar")
        self.icon_fechar.setGeometry(QRect(780, 30, 26, 26))
        self.icon_fechar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.icon_fechar.setPixmap(QPixmap(u":/icones/icons/fechar.png"))
        self.icon_fechar.setScaledContents(True)
        self.layoutWidget = QWidget(self.tela_registro)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(250, 130, 371, 231))
        self.box_input = QVBoxLayout(self.layoutWidget)
        self.box_input.setObjectName(u"box_input")
        self.box_input.setContentsMargins(0, 0, 0, 0)
        self.input_nome = QLineEdit(self.layoutWidget)
        self.input_nome.setObjectName(u"input_nome")

        self.box_input.addWidget(self.input_nome)

        self.input_sobrenome = QLineEdit(self.layoutWidget)
        self.input_sobrenome.setObjectName(u"input_sobrenome")
        self.input_sobrenome.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")

        self.box_input.addWidget(self.input_sobrenome)

        self.input_email = QLineEdit(self.layoutWidget)
        self.input_email.setObjectName(u"input_email")

        self.box_input.addWidget(self.input_email)

        self.input_senha = QLineEdit(self.layoutWidget)
        self.input_senha.setObjectName(u"input_senha")

        self.box_input.addWidget(self.input_senha)

        self.input_confirmar_senha = QLineEdit(self.layoutWidget)
        self.input_confirmar_senha.setObjectName(u"input_confirmar_senha")

        self.box_input.addWidget(self.input_confirmar_senha)


        self.retranslateUi(tela_principal_registro)

        QMetaObject.connectSlotsByName(tela_principal_registro)
    # setupUi

    def retranslateUi(self, tela_principal_registro):
        tela_principal_registro.setWindowTitle(QCoreApplication.translate("tela_principal_registro", u"Form", None))
        self.txt_boas_vindas.setText(QCoreApplication.translate("tela_principal_registro", u"Estamos felizes que voc\u00ea chegou aqui!\n"
"Crie sua conta para comprar ingressos e ganhar descontos", None))
        self.btn_registrar.setText(QCoreApplication.translate("tela_principal_registro", u"Registrar", None))
        self.icon_voltar.setText("")
        self.icon_fechar.setText("")
        self.input_nome.setPlaceholderText(QCoreApplication.translate("tela_principal_registro", u"Nome", None))
        self.input_sobrenome.setPlaceholderText(QCoreApplication.translate("tela_principal_registro", u"Sobrenome", None))
        self.input_email.setPlaceholderText(QCoreApplication.translate("tela_principal_registro", u"Email", None))
        self.input_senha.setPlaceholderText(QCoreApplication.translate("tela_principal_registro", u"Senha", None))
        self.input_confirmar_senha.setPlaceholderText(QCoreApplication.translate("tela_principal_registro", u"Confirmar senha", None))
    # retranslateUi

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_tela_principal_registro()
    window.show()
    sys.exit(app.exec())
