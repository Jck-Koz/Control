import mysql.connector
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QDateTime
from datetime import datetime
from .base_window_ui import Ui_TopLevel
from product.add_product_logic import AddProductLogic
from product.edit_product_logic import EditProductLogic
from database.database import create_connection, close_connection, check_connection


class BaseWindow(QMainWindow):
    def __init__(self, role, user_id):
        super(BaseWindow, self).__init__()
        self.ui = Ui_TopLevel()
        self.ui.setupUi(self)
        self.role = role
        self.user_id = user_id
        self.db_connection = create_connection()

        self.ui.search_button.clicked.connect(self.search_product)
        self.ui.search_bar.returnPressed.connect(self.search_product)

        # Configuración de la barra de navegación según el rol
        self.configure_nav_bar(role)

        self.ui.inicio.clicked.connect(
            lambda: self.update_active_page("inicio"))
        self.ui.productos.clicked.connect(
            lambda: self.update_active_page("productos"))
        self.ui.usuarios.clicked.connect(
            lambda: self.update_active_page("usuarios"))
        self.ui.reportes.clicked.connect(
            lambda: self.update_active_page("reportes"))

        self.load_products_table()
        self.load_combined_sales_table()

    def configure_nav_bar(self, role):
        print(f"Configuring navbar for role: {role}")
        print(f"Initial visibility - Usuarios: {self.ui.usuarios.isVisible()}, Productos: {
              self.ui.productos.isVisible()}, Reportes: {self.ui.reportes.isVisible()}")
        if role == 4:  # admin
            print("Role: admin - Showing all tabs")
            self.ui.inicio.setVisible(True)
            self.ui.productos.setVisible(True)
            self.ui.usuarios.setVisible(True)
            self.ui.reportes.setVisible(True)
        elif role == 3:  # caja
            print("Role: caja - Showing tabs: inicio, productos, reportes")
            self.ui.inicio.setVisible(True)
            self.ui.productos.setVisible(True)
            self.ui.usuarios.setVisible(False)
            self.ui.reportes.setVisible(True)
        elif role == 2:  # cliente
            print("Role: cliente - Showing tabs: inicio")
            self.ui.inicio.setVisible(True)
            self.ui.productos.setVisible(False)
            self.ui.usuarios.setVisible(False)
            self.ui.reportes.setVisible(False)
        elif role == 1:  # usuario
            print("Role: usuario - Showing tabs: inicio")
            self.ui.inicio.setVisible(True)
            self.ui.productos.setVisible(False)
            self.ui.usuarios.setVisible(False)
            self.ui.reportes.setVisible(False)
        print(f"After setting visibility - Usuarios: {self.ui.usuarios.isVisible()}, Productos: {
              self.ui.productos.isVisible()}, Reportes: {self.ui.reportes.isVisible()}")

    def update_active_page(self, page):
        if page == "inicio":
            self.ui.Paginas.setCurrentIndex(0)
        elif page == "productos":
            self.ui.Paginas.setCurrentIndex(1)
        elif page == "usuarios":
            self.ui.Paginas.setCurrentIndex(2)
        elif page == "reportes":
            self.ui.Paginas.setCurrentIndex(3)

    def search_product(self):
        barcode = self.ui.search_bar.text()
        if not barcode:
            QMessageBox.warning(
                self, "Error", "Por favor, ingrese un código de barras.")
            return

        self.db_connection = check_connection(self.db_connection)
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(
                "SELECT * FROM productos WHERE codigo_barras = %s", (barcode,))
            product = cursor.fetchone()

            if product:
                self.edit_product_window = EditProductLogic(product[0], self)
                self.edit_product_window.show()
            else:
                self.add_product_window = AddProductLogic(barcode, self)
                self.add_product_window.show()
                self.ui.search_bar.clear()
        except mysql.connector.Error as err:
            print(f"Error al buscar el producto: {err}")
            QMessageBox.warning(
                self, "Error", f"Error al buscar el producto: {err}")

    def load_products_table(self):
        self.db_connection = check_connection(self.db_connection)
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT p.nombre_producto, p.precio, c.nombre_categoria, m.nombre_marca, pr.nombre_proveedor, p.codigo_barras, 
                    CASE
                        WHEN ip.id_inventario IS NOT NULL THEN 'Ventas'
                        WHEN ii.id_inventario IS NOT NULL THEN 'Uso Interno'
                    END as inventario,
                    COALESCE(ip.cantidad, ii.cantidad) as cantidad, p.descripcion
                FROM productos p
                LEFT JOIN categorias c ON p.id_categoria = c.id_categoria
                LEFT JOIN marcas m ON p.id_marca = m.id_marca
                LEFT JOIN proveedores pr ON p.id_proveedor = pr.id_proveedor
                LEFT JOIN inventario_producto ip ON p.id_producto = ip.id_producto
                LEFT JOIN inventario_interno ii ON p.id_producto = ii.id_producto
            """)
            products = cursor.fetchall()

            self.ui.product_table.setRowCount(0)
            self.ui.product_table.setColumnCount(9)
            self.ui.product_table.setHorizontalHeaderLabels(
                ["Nombre", "Precio", "Categoría", "Marca", "Proveedor", "Código de Barras", "Inventario", "Cantidad", "Descripción"])

            for row_number, row_data in enumerate(products):
                self.ui.product_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.product_table.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))
        except mysql.connector.Error as err:
            print(f"Error al cargar los productos: {err}")
            QMessageBox.warning(
                self, "Error", f"Error al cargar los productos: {err}")

    def load_combined_sales_table(self):
        self.db_connection = check_connection(self.db_connection)
        try:
            cursor = self.db_connection.cursor()

            # Ventas
            cursor.execute("""
                SELECT v.id_venta, p.nombre_producto, u.nombre_usuario, v.cantidad, v.porcentaje_venta, v.fecha_venta, i.nombre_inventario, v.tipo
                FROM ventas v
                JOIN productos p ON v.id_producto = p.id_producto
                JOIN usuarios u ON v.id_usuario = u.id_usuario
                JOIN inventarios i ON v.id_inventario = i.id_inventario
            """)
            ventas = cursor.fetchall()

            # Ventas internas
            cursor.execute("""
                SELECT vi.id_venta, p.nombre_producto, u.nombre_usuario, vi.cantidad, vi.porcentaje_venta, vi.fecha_venta, i.nombre_inventario, vi.tipo
                FROM ventas_internas vi
                JOIN productos p ON vi.id_producto = p.id_producto
                JOIN usuarios u ON vi.id_usuario = u.id_usuario
                JOIN inventarios i ON vi.id_inventario = i.id_inventario
            """)
            ventas_internas = cursor.fetchall()

            combined_sales = ventas + ventas_internas

            # Convertir todas las fechas a datetime.datetime y manejar None
            for i, sale in enumerate(combined_sales):
                if sale[5] is not None:
                    if isinstance(sale[5], str):
                        combined_sales[i] = sale[:5] + \
                            (datetime.strptime(
                                sale[5], "%Y-%m-%d %H:%M:%S"),) + sale[6:]
                    elif isinstance(sale[5], QDateTime):
                        combined_sales[i] = sale[:5] + \
                            (sale[5].toPython(),) + sale[6:]
                else:
                    combined_sales[i] = sale[:5] + \
                        (datetime(1970, 1, 1, 0, 0, 0),) + sale[6:]

            combined_sales.sort(key=lambda x: x[5])  # Ordenar por fecha_venta

            self.ui.report_table.setRowCount(0)
            self.ui.report_table.setColumnCount(8)
            self.ui.report_table.setHorizontalHeaderLabels(
                ["ID Venta", "Producto", "Usuario", "Cantidad", "Porcentaje Venta", "Fecha Venta", "Inventario", "Tipo"])

            for row_number, row_data in enumerate(combined_sales):
                self.ui.report_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.report_table.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))
        except mysql.connector.Error as err:
            print(f"Error al cargar las ventas: {err}")
            QMessageBox.warning(
                self, "Error", f"Error al cargar las ventas: {err}")

    def closeEvent(self, event):
        try:
            close_connection()
        except Exception as e:
            print("Error al cerrar la conexión de la base de datos:", e)
        event.accept()
