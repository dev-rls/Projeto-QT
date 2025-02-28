# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Inicio.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import templates.img_inicio
class Ui_Inicio(object):
    def setupUi(self, Inicio):
        if not Inicio.objectName():
            Inicio.setObjectName(u"Inicio")
        Inicio.resize(869, 459)
        Inicio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.img_fundoTelaBemVindo = QLabel(Inicio)
        self.img_fundoTelaBemVindo.setObjectName(u"img_fundoTelaBemVindo")
        self.img_fundoTelaBemVindo.setGeometry(QRect(10, 0, 850, 450))
        self.img_fundoTelaBemVindo.setMaximumSize(QSize(899, 500))
        self.img_fundoTelaBemVindo.setAcceptDrops(False)
        self.img_fundoTelaBemVindo.setAutoFillBackground(False)
        self.img_fundoTelaBemVindo.setPixmap(QPixmap(u":/img_inicio/img_telaLogin.png"))
        self.img_fundoTelaBemVindo.setScaledContents(True)
        self.img_fundoTelaBemVindo.setWordWrap(False)
        self.input_criarConta = QLineEdit(Inicio)
        self.input_criarConta.setObjectName(u"input_criarConta")
        self.input_criarConta.setGeometry(QRect(230, 340, 331, 31))
        self.input_criarConta.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.btn_criarConta = QPushButton(Inicio)
        self.btn_criarConta.setObjectName(u"btn_criarConta")
        self.btn_criarConta.setGeometry(QRect(570, 340, 90, 30))
        self.btn_criarConta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_criarConta.setStyleSheet(u"QPushButton {\n"
"	font: 600 9pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(197, 68, 76);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(197, 68, 76);\n"
"}")
        self.txt_chamada = QLabel(Inicio)
        self.txt_chamada.setObjectName(u"txt_chamada")
        self.txt_chamada.setGeometry(QRect(230, 310, 431, 21))
        self.txt_chamada.setStyleSheet(u"\n"
"font: 900 16pt \"Segoe UI\";")
        self.btn_login = QPushButton(Inicio)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(760, 40, 90, 30))
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"\n"
"font: 600 9pt \"Segoe UI\";\n"
" color: rgb(197, 68, 76);\n"
" background-color: rgb(240, 240, 255);\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(197, 68, 76);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.txt_logo = QLabel(Inicio)
        self.txt_logo.setObjectName(u"txt_logo")
        self.txt_logo.setGeometry(QRect(50, 30, 171, 21))

        self.retranslateUi(Inicio)

        QMetaObject.connectSlotsByName(Inicio)
    # setupUi

    def retranslateUi(self, Inicio):
        Inicio.setWindowTitle(QCoreApplication.translate("Inicio", u"Form", None))
#if QT_CONFIG(whatsthis)
        self.img_fundoTelaBemVindo.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.img_fundoTelaBemVindo.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.img_fundoTelaBemVindo.setText("")
        self.input_criarConta.setPlaceholderText(QCoreApplication.translate("Inicio", u"Email", None))
        self.btn_criarConta.setText(QCoreApplication.translate("Inicio", u"Criar conta", None))
        self.txt_chamada.setText(QCoreApplication.translate("Inicio", u"Confira os filmes em cartaz nesta semana", None))
        self.btn_login.setText(QCoreApplication.translate("Inicio", u"Login", None))
        self.txt_logo.setText(QCoreApplication.translate("Inicio", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Bem Vindo</span><span style=\" font-size:12pt; font-weight:700; color:#c5444c;\"> PobreVision</span></p></body></html>", None))
    # retranslateUi

