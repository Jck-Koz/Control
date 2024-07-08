from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
                               QStackedWidget, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem)

import resources_rc


class Ui_TopLevel(object):
    def setupUi(self, TopLevel):
        if not TopLevel.objectName():
            TopLevel.setObjectName(u"TopLevel")
        TopLevel.resize(950, 570)
        self.centralwidget = QWidget(TopLevel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"QWidget{\n"
                                  "    background-color: rgb(31, 159, 239);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.inicio = QPushButton(self.header)
        self.inicio.setObjectName(u"inicio")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.inicio.setFont(font)
        self.inicio.setStyleSheet(u"QPushButton {\n"
                                  "    background-color: white;\n"
                                  "    color: rgb(31, 159, 239);\n"
                                  "    border: none;\n"
                                  "    border-radius: 8px;\n"
                                  "    padding: 5px;\n"
                                  "    margin: 5px;\n"
                                  "    font-weight: bold;\n"
                                  "}\n"
                                  "QPushButton:hover {\n"
                                  "    background-color: rgb(41, 128, 185);\n"
                                  "    color: white;\n"
                                  "}\n"
                                  "QPushButton:checked {\n"
                                  "    background-color: rgb(41, 128, 185);\n"
                                  "    color: white;\n"
                                  "}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/images/dashboard.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/newPrefix/images/dashboard_white.png",
                     QSize(), QIcon.Normal, QIcon.On)
        self.inicio.setIcon(icon)
        self.inicio.setCheckable(True)
        self.inicio.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.inicio)

        self.productos = QPushButton(self.header)
        self.productos.setObjectName(u"productos")
        self.productos.setFont(font)
        self.productos.setCursor(QCursor(Qt.PointingHandCursor))
        self.productos.setStyleSheet(u"QPushButton {\n"
                                     "    background-color: white;\n"
                                     "    color: rgb(31, 159, 239);\n"
                                     "    border: none;\n"
                                     "    border-radius: 8px;\n"
                                     "    padding: 5px;\n"
                                     "    margin: 5px;\n"
                                     "    font-weight: bold;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: rgb(41, 128, 185);\n"
                                     "    color: white;\n"
                                     "}\n"
                                     "QPushButton:checked {\n"
                                     "    background-color: rgb(41, 128, 185);\n"
                                     "    color: white;\n"
                                     "}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/images/settings.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/newPrefix/images/settings_white.png",
                      QSize(), QIcon.Normal, QIcon.On)
        self.productos.setIcon(icon1)
        self.productos.setCheckable(True)
        self.productos.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.productos)

        self.usuarios = QPushButton(self.header)
        self.usuarios.setObjectName(u"usuarios")
        self.usuarios.setFont(font)
        self.usuarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.usuarios.setStyleSheet(u"QPushButton {\n"
                                    "    background-color: white;\n"
                                    "    color: rgb(31, 159, 239);\n"
                                    "    border: none;\n"
                                    "    border-radius: 8px;\n"
                                    "    padding: 5px;\n"
                                    "    margin: 5px;\n"
                                    "    font-weight: bold;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(41, 128, 185);\n"
                                    "    color: white;\n"
                                    "}\n"
                                    "QPushButton:checked {\n"
                                    "    background-color: rgb(41, 128, 185);\n"
                                    "    color: white;\n"
                                    "}")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/images/profile.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/newPrefix/images/profile_white.png",
                      QSize(), QIcon.Normal, QIcon.On)
        self.usuarios.setIcon(icon2)
        self.usuarios.setCheckable(True)
        self.usuarios.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.usuarios)

        self.reportes = QPushButton(self.header)
        self.reportes.setObjectName(u"reportes")
        self.reportes.setFont(font)
        self.reportes.setCursor(QCursor(Qt.PointingHandCursor))
        self.reportes.setStyleSheet(u"QPushButton {\n"
                                    "    background-color: white;\n"
                                    "    color: rgb(31, 159, 239);\n"
                                    "    border: none;\n"
                                    "    border-radius: 8px;\n"
                                    "    padding: 5px;\n"
                                    "    margin: 5px;\n"
                                    "    font-weight: bold;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(41, 128, 185);\n"
                                    "    color: white;\n"
                                    "}\n"
                                    "QPushButton:checked {\n"
                                    "    background-color: rgb(41, 128, 185);\n"
                                    "    color: white;\n"
                                    "}")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/images/messages.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/newPrefix/images/messages_white.png",
                      QSize(), QIcon.Normal, QIcon.On)
        self.reportes.setIcon(icon3)
        self.reportes.setCheckable(True)
        self.reportes.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.reportes)

        self.horizontalSpacer = QSpacerItem(
            236, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.searchlayout = QHBoxLayout()
        self.searchlayout.setSpacing(0)
        self.searchlayout.setObjectName(u"searchlayout")
        self.search_bar = QLineEdit(self.header)
        self.search_bar.setObjectName(u"search_bar")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.search_bar.setFont(font1)
        self.search_bar.setStyleSheet(u"QLineEdit {\n"
                                      "    background-color: white;\n"
                                      "    border: none;\n"
                                      "    border-radius: 8px;\n"
                                      "    padding: 5px;\n"
                                      "    margin: 5px;\n"
                                      "    color: rgb(31, 159, 239);\n"
                                      "}")

        self.searchlayout.addWidget(self.search_bar)

        self.search_button = QPushButton(self.header)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_button.setStyleSheet(u"QPushButton {\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(31, 159, 239);\n"
                                         "    border: none;\n"
                                         "    border-radius: 8px;\n"
                                         "    padding: 5px;\n"
                                         "    margin: 5px;\n"
                                         "    font-weight: bold;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(41, 128, 185);\n"
                                         "    color: white;\n"
                                         "}")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/images/search.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon4)
        self.search_button.setIconSize(QSize(20, 20))

        self.searchlayout.addWidget(self.search_button)

        self.horizontalLayout.addLayout(self.searchlayout)

        self.perfilbutton = QPushButton(self.header)
        self.perfilbutton.setObjectName(u"perfilbutton")
        self.perfilbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.perfilbutton.setStyleSheet(u"QPushButton {\n"
                                        "    background-color: white;\n"
                                        "    color: rgb(31, 159, 239);\n"
                                        "    border: none;\n"
                                        "    border-radius: 8px;\n"
                                        "    padding: 5px;\n"
                                        "    margin: 5px;\n"
                                        "    font-weight: bold;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(41, 128, 185);\n"
                                        "    color: white;\n"
                                        "}")
        self.perfilbutton.setIcon(icon2)
        self.perfilbutton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.perfilbutton)

        self.verticalLayout.addWidget(self.header)

        self.Body = QWidget(self.centralwidget)
        self.Body.setObjectName(u"Body")
        self.horizontalLayout_2 = QHBoxLayout(self.Body)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Paginas = QStackedWidget(self.Body)
        self.Paginas.setObjectName(u"Paginas")
        self.Paginas.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.inicio_page = QWidget()
        self.inicio_page.setObjectName(u"inicio_page")
        self.gridLayout_6 = QGridLayout(self.inicio_page)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Paginas.addWidget(self.inicio_page)
        self.productos_page = QWidget()
        self.productos_page.setObjectName(u"productos_page")
        self.gridLayout_4 = QGridLayout(self.productos_page)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)

        self.product_table = QTableWidget(self.productos_page)
        self.product_table.setObjectName(u"product_table")
        self.gridLayout_4.addWidget(self.product_table, 0, 0, 1, 1)

        self.Paginas.addWidget(self.productos_page)
        self.usuarios_page = QWidget()
        self.usuarios_page.setObjectName(u"usuarios_page")
        self.gridLayout_5 = QGridLayout(self.usuarios_page)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Paginas.addWidget(self.usuarios_page)
        self.reportes_page = QWidget()
        self.reportes_page.setObjectName(u"reportes_page")
        self.gridLayout_3 = QGridLayout(self.reportes_page)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.report_table = QTableWidget(self.reportes_page)
        self.report_table.setObjectName(u"report_table")
        self.gridLayout_3.addWidget(self.report_table, 0, 0, 1, 1)

        self.Paginas.addWidget(self.reportes_page)

        self.horizontalLayout_2.addWidget(self.Paginas)

        self.verticalLayout.addWidget(self.Body)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        TopLevel.setCentralWidget(self.centralwidget)

        self.retranslateUi(TopLevel)

        self.Paginas.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(TopLevel)
    # setupUi

    def retranslateUi(self, TopLevel):
        TopLevel.setWindowTitle(QCoreApplication.translate(
            "TopLevel", u"BaseWindow", None))
        self.inicio.setText(QCoreApplication.translate(
            "TopLevel", u"Inicio", None))
        self.productos.setText(QCoreApplication.translate(
            "TopLevel", u"Productos", None))
        self.usuarios.setText(QCoreApplication.translate(
            "TopLevel", u"Usuarios", None))
        self.reportes.setText(QCoreApplication.translate(
            "TopLevel", u"Reportes", None))
        self.search_bar.setPlaceholderText(
            QCoreApplication.translate("TopLevel", u"Buscar...", None))
        self.search_button.setText("")
        self.perfilbutton.setText("")
