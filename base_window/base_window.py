import mysql.connector
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from .base_window_ui import Ui_TopLevel
from product.add_product_logic import AddProductLogic
from product.edit_product_logic import EditProductLogic
from database.database import create_connection, close_connection, check_connection


class BaseWindow(QMainWindow):
    def __init__(self, role):
        super(BaseWindow, self).__init__()
        self.ui = Ui_TopLevel()
        self.ui.setupUi(self)
        self.role = role
        self.db_connection = create_connection()

        self.ui.search_button.clicked.connect(self.search_product)
        self.ui.search_bar.returnPressed.connect(self.search_product)

        self.ui.inicio.clicked.connect(
            lambda: self.update_active_page("inicio"))
        self.ui.productos.clicked.connect(
            lambda: self.update_active_page("productos"))
        self.ui.usuarios.clicked.connect(
            lambda: self.update_active_page("usuarios"))
        self.ui.reportes.clicked.connect(
            lambda: self.update_active_page("reportes"))

        self.load_products_table()
        self.load_sales_table()

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

    def load_sales_table(self):
        self.db_connection = check_connection(self.db_connection)
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT v.id_venta, p.nombre_producto, u.nombre_usuario, v.cantidad, v.porcentaje_venta, v.fecha_venta, i.nombre_inventario
                FROM ventas v
                JOIN productos p ON v.id_producto = p.id_producto
                JOIN usuarios u ON v.id_usuario = u.id_usuario
                JOIN inventarios i ON v.id_inventario = i.id_inventario
            """)
            sales = cursor.fetchall()

            self.ui.report_table.setRowCount(0)
            self.ui.report_table.setColumnCount(7)
            self.ui.report_table.setHorizontalHeaderLabels(
                ["ID Venta", "Producto", "Usuario", "Cantidad", "Porcentaje Venta", "Fecha Venta", "Inventario"])

            for row_number, row_data in enumerate(sales):
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
            close_connection(self.db_connection)
            print("Database connection closed.")
        except Exception as e:
            print("Error al cerrar la conexión de la base de datos:", e)
        event.accept()
