# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerXHKZVY.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(29, 60, 341, 201))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.pushButton_6, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.pushButton_5, 1, 3, 1, 1)

        self.PUSH = QPushButton(self.gridLayoutWidget)
        self.PUSH.setObjectName(u"PUSH")
        self.PUSH.setEnabled(True)
        self.PUSH.setMaximumSize(QSize(30, 30))
        self.PUSH.setStyleSheet(u"QPushButton ({chr(65 + linha)}{coluna + 1;\n"
"})")

        self.gridLayout.addWidget(self.PUSH, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.pushButton_10, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.pushButton_8, 2, 3, 1, 1)


        self.retranslateUi(Form)

        self.pushButton_7.setDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_5.setDefault(False)
        self.PUSH.setDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton_10.setDefault(False)
        self.pushButton_9.setDefault(False)
        self.pushButton_8.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"B4", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"A3", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"B1", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"B5", None))
        self.PUSH.setText(QCoreApplication.translate("Form", u"A2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"B3", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"C1", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"C2", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"C3", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"C4", None))
    # retranslateUi
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

''''''
from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication

class TelaAssentos(QWidget):
    def __init__(self):
        super().__init__()

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        for linha in range(4):
            for coluna in range(6):
                botao_assento = QPushButton(f"{chr(65 + linha)}{coluna + 1}") # Cria os botoes com nomes de A1, A2, B1 etc
                botao_assento.setMaximumSize(30, 30) # Define o tamanho maximo
                self.grid_layout.addWidget(botao_assento, linha, coluna)

if __name__ == "__main__":
    app = QApplication([])
    tela_assentos = TelaAssentos()
    tela_assentos.show()
    app.exec_()

