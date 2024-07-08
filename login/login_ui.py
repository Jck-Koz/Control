from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtGui import QFont, QCursor
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QCheckBox, QSizePolicy, QSpacerItem


class Ui_Windowlogin(object):
    def setupUi(self, Windowlogin):
        if not Windowlogin.objectName():
            Windowlogin.setObjectName(u"Windowlogin")
        Windowlogin.resize(439, 180)
        font = QFont()
        font.setBold(True)
        Windowlogin.setFont(font)
        Windowlogin.setStyleSheet(u"")
        self.centralwidget = QWidget(Windowlogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(
            u"background-color: rgb(29, 147, 221);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 15, 10, 10)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, -1, 6, -1)
        self.labelusername = QLabel(self.centralwidget)
        self.labelusername.setObjectName(u"labelusername")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.labelusername.setFont(font1)
        self.labelusername.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayout_2.addWidget(self.labelusername)
        self.labelpass = QLabel(self.centralwidget)
        self.labelpass.setObjectName(u"labelpass")
        self.labelpass.setFont(font1)
        self.labelpass.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayout_2.addWidget(self.labelpass)
        self.labelremember = QLabel(self.centralwidget)
        self.labelremember.setObjectName(u"labelremember")
        self.labelremember.setFont(font1)
        self.labelremember.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayout_2.addWidget(self.labelremember)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 6, 0)
        self.lineEditusername = QLineEdit(self.centralwidget)
        self.lineEditusername.setObjectName(u"lineEditusername")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.lineEditusername.setFont(font2)
        self.lineEditusername.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                            "border:none;\n"
                                            "border-radius:8px;\n"
                                            "padding:3px;\n"
                                            "color: rgb(31, 159, 239);\n"
                                            "margin:5px;\n"
                                            "")
        self.verticalLayout.addWidget(self.lineEditusername)
        self.lineEditpass = QLineEdit(self.centralwidget)
        self.lineEditpass.setObjectName(u"lineEditpass")
        self.lineEditpass.setFont(font2)
        self.lineEditpass.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                        "border:none;\n"
                                        "border-radius:8px;\n"
                                        "padding:3px;\n"
                                        "color: rgb(31, 159, 239);\n"
                                        "margin:5px;\n"
                                        "")
        self.lineEditpass.setEchoMode(QLineEdit.EchoMode.Password)
        self.verticalLayout.addWidget(self.lineEditpass)
        self.rememberMe = QCheckBox(self.centralwidget)
        self.rememberMe.setObjectName(u"rememberMe")
        self.rememberMe.setFont(font2)
        self.rememberMe.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayout.addWidget(self.rememberMe)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 15)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer)
        self.Iniciarsesion = QPushButton(self.centralwidget)
        self.Iniciarsesion.setObjectName(u"Iniciarsesion")
        self.Iniciarsesion.setFont(font1)
        self.Iniciarsesion.setCursor(QCursor(Qt.PointingHandCursor))
        self.Iniciarsesion.setStyleSheet(u"QPushButton {\n"
                                         "	background-color: rgb(255, 255, 255);\n"
                                         "    color: rgb(31, 159, 239);\n"
                                         "    border:none;\n"
                                         "	padding:5px;	\n"
                                         "	border-radius:8px;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "	background-color: rgb(29, 147, 221);\n"
                                         "	 color: rgb(255, 255, 255);\n"
                                         "     border:none;\n"
                                         "}")
        self.horizontalLayout_2.addWidget(self.Iniciarsesion)
        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        Windowlogin.setCentralWidget(self.centralwidget)
        self.retranslateUi(Windowlogin)
        QMetaObject.connectSlotsByName(Windowlogin)

    def retranslateUi(self, Windowlogin):
        Windowlogin.setWindowTitle(
            QCoreApplication.translate("Windowlogin", u"login", None))
        self.labelusername.setText(QCoreApplication.translate(
            "Windowlogin", u"      Usuario:", None))
        self.labelpass.setText(QCoreApplication.translate(
            "Windowlogin", u"Contrase\u00f1a:", None))
        self.lineEditusername.setPlaceholderText(QCoreApplication.translate(
            "Windowlogin", u"   Nombre De Usuario...", None))
        self.lineEditpass.setPlaceholderText(QCoreApplication.translate(
            "Windowlogin", u"   Contrase\u00f1a...", None))
        self.rememberMe.setText(QCoreApplication.translate(
            "Windowlogin", u"   Recordar Contraseña", None))
        self.Iniciarsesion.setText(QCoreApplication.translate(
            "Windowlogin", u"Iniciar Sesi\u00f3n", None))
