# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

import templates.fundo_login_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(896, 511)
        self.img_fundo_login = QLabel(Login)
        self.img_fundo_login.setObjectName(u"img_fundo_login")
        self.img_fundo_login.setGeometry(QRect(20, 0, 850, 500))
        self.img_fundo_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.img_fundo_login.setAutoFillBackground(False)
        self.img_fundo_login.setStyleSheet(u"background-color: rgb(197, 68, 76);")
        self.img_fundo_login.setPixmap(QPixmap(u":/fundo_login/imagens/img_telaLogin.png"))
        self.img_fundo_login.setScaledContents(True)
        self.img_fundo_login.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.btn_esqueceu_senha = QLabel(Login)
        self.btn_esqueceu_senha.setObjectName(u"btn_esqueceu_senha")
        self.btn_esqueceu_senha.setGeometry(QRect(480, 320, 101, 21))
        self.btn_esqueceu_senha.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_esqueceu_senha.setStyleSheet(u"font: 600 9pt \"Segoe UI\";")
        self.txt_faca_login = QLabel(Login)
        self.txt_faca_login.setObjectName(u"txt_faca_login")
        self.txt_faca_login.setGeometry(QRect(340, 140, 211, 51))
        self.btn_entrar = QPushButton(Login)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(390, 380, 90, 30))
        self.btn_entrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_entrar.setStyleSheet(u"QPushButton {\n"
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
"\n"
"\n"
"")
        self.btn_lembrar = QCheckBox(Login)
        self.btn_lembrar.setObjectName(u"btn_lembrar")
        self.btn_lembrar.setGeometry(QRect(320, 320, 78, 20))
        self.btn_lembrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_lembrar.setStyleSheet(u"font: 600 9pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255)")
        
        self.layoutWidget = QWidget(Login)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(310, 230, 271, 42))
        self.box_user = QHBoxLayout(self.layoutWidget)
        self.box_user.setObjectName(u"box_user")
        self.box_user.setContentsMargins(0, 0, 0, 0)
        self.icon_user = QLabel(self.layoutWidget)
        self.icon_user.setObjectName(u"icon_user")
        self.icon_user.setPixmap(QPixmap(u":/fundo_login/icons/user.png"))
        self.icon_user.setScaledContents(True)

        self.box_user.addWidget(self.icon_user)

        self.input_user = QLineEdit(self.layoutWidget)
        self.input_user.setObjectName(u"input_user")
        self.input_user.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")

        self.box_user.addWidget(self.input_user)

        self.layoutWidget1 = QWidget(Login)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(310, 270, 271, 32))
        self.box_senha = QHBoxLayout(self.layoutWidget1)
        self.box_senha.setObjectName(u"box_senha")
        self.box_senha.setContentsMargins(0, 0, 0, 0)
        self.icon_cadeado = QLabel(self.layoutWidget1)
        self.icon_cadeado.setObjectName(u"icon_cadeado")
        self.icon_cadeado.setPixmap(QPixmap(u":/fundo_login/icons/cadeado_p.png"))
        self.icon_cadeado.setScaledContents(True)

        self.box_senha.addWidget(self.icon_cadeado)

        self.input_senha = QLineEdit(self.layoutWidget1)
        self.input_senha.setObjectName(u"input_senha")
        self.input_senha.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.input_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.box_senha.addWidget(self.input_senha)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Dialog", None))
        self.img_fundo_login.setText("")
        self.btn_esqueceu_senha.setText(QCoreApplication.translate("Login", u"Esqueceu a senha?", None))
        self.txt_faca_login.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700; color:#c38521;\">FA\u00c7A LOGIN</span><span style=\" font-size:28pt;\"/></p></body></html>", None))
        self.btn_entrar.setText(QCoreApplication.translate("Login", u"Entrar", None))
        self.btn_lembrar.setText(QCoreApplication.translate("Login", u"Lembrar", None))
        self.icon_user.setText("")
        self.input_user.setPlaceholderText(QCoreApplication.translate("Login", u"Digite seu usu\u00e1rio", None))
        self.icon_cadeado.setText("")
        self.input_senha.setPlaceholderText(QCoreApplication.translate("Login", u"Digite sua senha", None))
    # retranslateUi

