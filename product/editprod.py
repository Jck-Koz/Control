# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editprod.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_EditProductWindow(object):
    def setupUi(self, EditProductWindow):
        if not EditProductWindow.objectName():
            EditProductWindow.setObjectName(u"EditProductWindow")
        EditProductWindow.resize(439, 490)
        self.centralwidget = QWidget(EditProductWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(31, 159, 244);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_10 = QWidget(self.centralwidget)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"height:30px")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.labelNombre = QLabel(self.widget_10)
        self.labelNombre.setObjectName(u"labelNombre")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.labelNombre.setFont(font)
        self.labelNombre.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"height:30px")

        self.horizontalLayout_10.addWidget(self.labelNombre, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.widget_10)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelInventario = QLabel(self.widget)
        self.labelInventario.setObjectName(u"labelInventario")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.labelInventario.setFont(font1)
        self.labelInventario.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout.addWidget(self.labelInventario, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.widget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelPrecio = QLabel(self.widget_3)
        self.labelPrecio.setObjectName(u"labelPrecio")
        self.labelPrecio.setFont(font1)
        self.labelPrecio.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_3.addWidget(self.labelPrecio, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelDescripcion = QLabel(self.widget_4)
        self.labelDescripcion.setObjectName(u"labelDescripcion")
        self.labelDescripcion.setFont(font1)
        self.labelDescripcion.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_4.addWidget(self.labelDescripcion, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelCodigoBarras = QLabel(self.widget_5)
        self.labelCodigoBarras.setObjectName(u"labelCodigoBarras")
        self.labelCodigoBarras.setFont(font1)
        self.labelCodigoBarras.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_5.addWidget(self.labelCodigoBarras, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.widget_5)

        self.widget_9 = QWidget(self.centralwidget)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.labelCategoria = QLabel(self.widget_9)
        self.labelCategoria.setObjectName(u"labelCategoria")
        self.labelCategoria.setFont(font1)
        self.labelCategoria.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_9.addWidget(self.labelCategoria, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.widget_9)

        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelMarca = QLabel(self.widget_6)
        self.labelMarca.setObjectName(u"labelMarca")
        self.labelMarca.setFont(font1)
        self.labelMarca.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_6.addWidget(self.labelMarca, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.labelProveedor = QLabel(self.widget_7)
        self.labelProveedor.setObjectName(u"labelProveedor")
        self.labelProveedor.setFont(font1)
        self.labelProveedor.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_7.addWidget(self.labelProveedor, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.centralwidget)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.labelCantidad = QLabel(self.widget_8)
        self.labelCantidad.setObjectName(u"labelCantidad")
        self.labelCantidad.setFont(font1)
        self.labelCantidad.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_8.addWidget(self.labelCantidad, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.widget_8)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelPorcentajeOperacion = QLabel(self.widget_2)
        self.labelPorcentajeOperacion.setObjectName(u"labelPorcentajeOperacion")
        self.labelPorcentajeOperacion.setFont(font1)
        self.labelPorcentajeOperacion.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_2.addWidget(self.labelPorcentajeOperacion, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.widget_2)


        self.horizontalLayout_13.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.widget_21 = QWidget(self.centralwidget)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.nombreInput = QLineEdit(self.widget_21)
        self.nombreInput.setObjectName(u"nombreInput")
        self.nombreInput.setMinimumSize(QSize(239, 0))
        self.nombreInput.setFont(font1)
        self.nombreInput.setStyleSheet(u"border-radius:8px;\n"
"color: rgb(31, 159, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"height:30px\n"
"")

        self.horizontalLayout_12.addWidget(self.nombreInput)


        self.verticalLayout_2.addWidget(self.widget_21)

        self.widget_22 = QWidget(self.centralwidget)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.inventarioInput = QComboBox(self.widget_22)
        self.inventarioInput.setObjectName(u"inventarioInput")
        self.inventarioInput.setMinimumSize(QSize(239, 0))
        self.inventarioInput.setFont(font1)
        self.inventarioInput.setStyleSheet(u"border-radius:8px;\n"
"color: rgb(31, 159, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"height:30px")

        self.horizontalLayout_16.addWidget(self.inventarioInput)


        self.verticalLayout_2.addWidget(self.widget_22)

        self.widget_23 = QWidget(self.centralwidget)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.precioInput = QLineEdit(self.widget_23)
        self.precioInput.setObjectName(u"precioInput")
        self.precioInput.setMinimumSize(QSize(239, 0))
        self.precioInput.setFont(font1)
        self.precioInput.setStyleSheet(u"border-radius:8px;\n"
"color: rgb(31, 159, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"height:30px")

        self.horizontalLayout_17.addWidget(self.precioInput)


        self.verticalLayout_2.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.centralwidget)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.descripcionInput = QLineEdit(self.widget_24)
        self.descripcionInput.setObjectName(u"descripcionInput")
        self.descripcionInput.setMinimumSize(QSize(239, 0))
        self.descripcionInput.setFont(font1)
        self.descripcionInput.setStyleSheet(u"border-radius:8px;\n"
"color: rgb(31, 159, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"height:30px")

        self.horizontalLayout_18.addWidget(self.descripcionInput)


        self.verticalLayout_2.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.centralwidget)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.codigoBarrasInput = QLineEdit(self.widget_25)
        self.codigoBarrasInput.setObjectName(u"codigoBarrasInput")
        self.codigoBarrasInput.setMinimumSize(QSize(239, 0))
        self.codigoBarrasInput.setFont(font1)
        self.codigoBarrasInput.setStyleSheet(u"border-radius:8px;\n"
"color: rgb(31, 159, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"height:30px")

        self.horizontalLayout_25.addWidget(self.codigoBarrasInput)


        self.verticalLayout_2.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.centralwidget)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setStyleSheet(u"")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.categoriaInput = QComboBox(self.widget_26)
        self.categoriaInput.setObjectName(u"categoriaInput")
        self.categoriaInput.setMinimumSize(QSize(239, 0))
        self.categoriaInput.setFont(font1)
        self.categoriaInput.setStyleSheet(u"border-radius:8px;\n"
"color: rgb(31, 159, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"height:30px")

        self.horizontalLayout_26.addWidget(self.categoriaInput)


        self.verticalLayout_2.addWidget(self.widget_26)

        self.widget_27 = QWidget(self.centralwidget)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.marcaInput = QComboBox(self.widget_27)
        self.marcaInput.setObjectName(u"marcaInput")
        self.marcaInput.setMinimumSize(QSize(239, 0))
        self.marcaInput.setFont(font1)
        self.marcaInput.setStyleSheet(u"border-radius:8px;\n"
"color: rgb(31, 159, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"height:30px")

        self.horizontalLayout_27.addWidget(self.marcaInput)


        self.verticalLayout_2.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.centralwidget)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.proveedorInput = QComboBox(self.widget_28)
        self.proveedorInput.setObjectName(u"proveedorInput")
        self.proveedorInput.setMinimumSize(QSize(239, 0))
        self.proveedorInput.setFont(font1)
        self.proveedorInput.setStyleSheet(u"border-radius:8px;\n"
"color: rgb(31, 159, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"height:30px")

        self.horizontalLayout_28.addWidget(self.proveedorInput)


        self.verticalLayout_2.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.centralwidget)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.cantidadInput = QSpinBox(self.widget_29)
        self.cantidadInput.setObjectName(u"cantidadInput")
        self.cantidadInput.setFont(font1)
        self.cantidadInput.setStyleSheet(u"border-radius:8px;\n"
"color: rgb(31, 159, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"height:30px")
        self.cantidadInput.setMinimum(1)
        self.cantidadInput.setMaximum(1000)

        self.horizontalLayout_29.addWidget(self.cantidadInput)


        self.verticalLayout_2.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.centralwidget)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.porcentajeOperacionInput = QLineEdit(self.widget_30)
        self.porcentajeOperacionInput.setObjectName(u"porcentajeOperacionInput")
        self.porcentajeOperacionInput.setMinimumSize(QSize(239, 0))
        self.porcentajeOperacionInput.setFont(font1)
        self.porcentajeOperacionInput.setStyleSheet(u"border-radius:8px;\n"
"color: rgb(31, 159, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"height:30px")

        self.horizontalLayout_30.addWidget(self.porcentajeOperacionInput)


        self.verticalLayout_2.addWidget(self.widget_30)


        self.horizontalLayout_13.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, -1, 5, -1)
        self.widget_11 = QWidget(self.centralwidget)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")

        self.verticalLayout_3.addWidget(self.widget_11)

        self.widget_31 = QWidget(self.centralwidget)
        self.widget_31.setObjectName(u"widget_31")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.widget_31)

        self.widget_13 = QWidget(self.centralwidget)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")

        self.verticalLayout_3.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.centralwidget)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")

        self.verticalLayout_3.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.centralwidget)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")

        self.verticalLayout_3.addWidget(self.widget_15)

        self.widget_32 = QWidget(self.centralwidget)
        self.widget_32.setObjectName(u"widget_32")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.categoriaButton = QPushButton(self.widget_32)
        self.categoriaButton.setObjectName(u"categoriaButton")
        self.categoriaButton.setEnabled(True)
        self.categoriaButton.setMinimumSize(QSize(41, 0))
        self.categoriaButton.setMaximumSize(QSize(41, 16777215))
        self.categoriaButton.setFont(font1)
        self.categoriaButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.categoriaButton.setStyleSheet(u"border-radius:8px;\n"
"color: rgb(31, 159, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.categoriaButton.setAutoDefault(False)
        self.categoriaButton.setFlat(False)

        self.horizontalLayout_32.addWidget(self.categoriaButton)


        self.verticalLayout_3.addWidget(self.widget_32)

        self.widget_33 = QWidget(self.centralwidget)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.marcaButton = QPushButton(self.widget_33)
        self.marcaButton.setObjectName(u"marcaButton")
        self.marcaButton.setEnabled(True)
        self.marcaButton.setMinimumSize(QSize(41, 0))
        self.marcaButton.setMaximumSize(QSize(41, 16777215))
        self.marcaButton.setFont(font1)
        self.marcaButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.marcaButton.setStyleSheet(u"border-radius:8px;\n"
"color: rgb(31, 159, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.marcaButton.setAutoDefault(False)
        self.marcaButton.setFlat(False)

        self.horizontalLayout_33.addWidget(self.marcaButton)


        self.verticalLayout_3.addWidget(self.widget_33)

        self.widget_34 = QWidget(self.centralwidget)
        self.widget_34.setObjectName(u"widget_34")
        self.ProveedorButton = QPushButton(self.widget_34)
        self.ProveedorButton.setObjectName(u"ProveedorButton")
        self.ProveedorButton.setEnabled(True)
        self.ProveedorButton.setGeometry(QRect(0, 9, 41, 26))
        self.ProveedorButton.setMinimumSize(QSize(41, 0))
        self.ProveedorButton.setMaximumSize(QSize(41, 16777215))
        self.ProveedorButton.setFont(font1)
        self.ProveedorButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ProveedorButton.setStyleSheet(u"border-radius:8px;\n"
"color: rgb(31, 159, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.ProveedorButton.setAutoDefault(False)
        self.ProveedorButton.setFlat(False)

        self.verticalLayout_3.addWidget(self.widget_34)

        self.widget_19 = QWidget(self.centralwidget)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")

        self.verticalLayout_3.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.centralwidget)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")

        self.verticalLayout_3.addWidget(self.widget_20)


        self.horizontalLayout_13.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.widget_12 = QWidget(self.centralwidget)
        self.widget_12.setObjectName(u"widget_12")
        self.EntradaButton = QPushButton(self.widget_12)
        self.EntradaButton.setObjectName(u"EntradaButton")
        self.EntradaButton.setGeometry(QRect(50, 10, 150, 30))
        self.EntradaButton.setMinimumSize(QSize(150, 0))
        self.EntradaButton.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.EntradaButton.setFont(font2)
        self.EntradaButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.EntradaButton.setStyleSheet(u"border-radius:8px;\n"
"color: rgb(31, 159, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"height:30px;")
        self.salidaButton = QPushButton(self.widget_12)
        self.salidaButton.setObjectName(u"salidaButton")
        self.salidaButton.setGeometry(QRect(240, 10, 150, 30))
        self.salidaButton.setMinimumSize(QSize(150, 0))
        self.salidaButton.setMaximumSize(QSize(150, 16777215))
        self.salidaButton.setFont(font2)
        self.salidaButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.salidaButton.setStyleSheet(u"border-radius:8px;\n"
"color: rgb(31, 159, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"height:30px;")

        self.verticalLayout_5.addWidget(self.widget_12)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        EditProductWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditProductWindow)

        self.categoriaButton.setDefault(True)
        self.marcaButton.setDefault(True)
        self.ProveedorButton.setDefault(True)


        QMetaObject.connectSlotsByName(EditProductWindow)
    # setupUi

    def retranslateUi(self, EditProductWindow):
        EditProductWindow.setWindowTitle(QCoreApplication.translate("EditProductWindow", u"Editar Producto", None))
        self.labelNombre.setText(QCoreApplication.translate("EditProductWindow", u"Nombre:", None))
        self.labelInventario.setText(QCoreApplication.translate("EditProductWindow", u"Inventario:", None))
        self.labelPrecio.setText(QCoreApplication.translate("EditProductWindow", u"Precio:", None))
        self.labelDescripcion.setText(QCoreApplication.translate("EditProductWindow", u"Descripci\u00f3n:", None))
        self.labelCodigoBarras.setText(QCoreApplication.translate("EditProductWindow", u"C\u00f3digo:", None))
        self.labelCategoria.setText(QCoreApplication.translate("EditProductWindow", u"Categor\u00eda:", None))
        self.labelMarca.setText(QCoreApplication.translate("EditProductWindow", u"Marca:", None))
        self.labelProveedor.setText(QCoreApplication.translate("EditProductWindow", u"Proveedor:", None))
        self.labelCantidad.setText(QCoreApplication.translate("EditProductWindow", u"Cantidad:", None))
        self.labelPorcentajeOperacion.setText(QCoreApplication.translate("EditProductWindow", u"Porcentaje:", None))
        self.categoriaButton.setText(QCoreApplication.translate("EditProductWindow", u"+", None))
        self.marcaButton.setText(QCoreApplication.translate("EditProductWindow", u"+", None))
        self.ProveedorButton.setText(QCoreApplication.translate("EditProductWindow", u"+", None))
        self.EntradaButton.setText(QCoreApplication.translate("EditProductWindow", u"Entrada", None))
        self.salidaButton.setText(QCoreApplication.translate("EditProductWindow", u"Salida", None))
    # retranslateUi

