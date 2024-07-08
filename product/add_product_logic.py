import mysql.connector
from PySide6.QtWidgets import QMainWindow, QMessageBox, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel
from .addprod import Ui_AddProductWindow
from database.database import create_connection, close_connection, check_connection


class AddProductLogic(QMainWindow):
    def __init__(self, barcode, main_window):
        super(AddProductLogic, self).__init__()
        self.ui = Ui_AddProductWindow()
        self.ui.setupUi(self)
        self.db_connection = create_connection()
        self.main_window = main_window  # Referencia a la ventana principal
        self.ui.codigoBarrasInput.setText(barcode)
        self.populate_comboboxes()
        self.ui.agregarButton.clicked.connect(self.add_product)
        self.ui.categoriaButton.clicked.connect(self.add_category)
        self.ui.marcaButton.clicked.connect(self.add_brand)
        self.ui.ProveedorButton.clicked.connect(self.add_supplier)

    def populate_comboboxes(self):
        self.db_connection = check_connection(self.db_connection)
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT nombre_categoria FROM categorias")
            categories = cursor.fetchall()
            for category in categories:
                self.ui.categoriaInput.addItem(category[0])

            cursor.execute("SELECT nombre_marca FROM marcas")
            brands = cursor.fetchall()
            for brand in brands:
                self.ui.marcaInput.addItem(brand[0])

            cursor.execute("SELECT nombre_proveedor FROM proveedores")
            suppliers = cursor.fetchall()
            for supplier in suppliers:
                self.ui.proveedorInput.addItem(supplier[0])

            cursor.execute("SELECT nombre_inventario FROM inventarios")
            inventories = cursor.fetchall()
            for inventory in inventories:
                self.ui.inventarioInput.addItem(inventory[0])

        except mysql.connector.Error as err:
            print(f"Error al poblar los comboboxes: {err}")

    def add_product(self):
        self.db_connection = check_connection(self.db_connection)
        nombre = self.ui.nombreInput.text()
        descripcion = self.ui.descripcionInput.text()
        precio = self.ui.precioInput.text()
        codigo_barras = self.ui.codigoBarrasInput.text()
        categoria = self.ui.categoriaInput.currentText()
        marca = self.ui.marcaInput.currentText()
        proveedor = self.ui.proveedorInput.currentText()
        inventario = self.ui.inventarioInput.currentText()
        cantidad = self.ui.cantidadInput.value()
        porcentaje_operacion = self.ui.porcentajeOperacionInput.text()

        if not all([nombre, precio, codigo_barras, categoria, marca, proveedor, inventario, cantidad]):
            QMessageBox.warning(
                self, "Error", "Los campos obligatorios deben ser llenados.")
            return

        try:
            cursor = self.db_connection.cursor()
            cursor.execute(
                "SELECT id_categoria FROM categorias WHERE nombre_categoria = %s", (categoria,))
            id_categoria = cursor.fetchone()[0]
            cursor.execute(
                "SELECT id_marca FROM marcas WHERE nombre_marca = %s", (marca,))
            id_marca = cursor.fetchone()[0]
            cursor.execute(
                "SELECT id_proveedor FROM proveedores WHERE nombre_proveedor = %s", (proveedor,))
            id_proveedor = cursor.fetchone()[0]
            cursor.execute(
                "SELECT id_inventario FROM inventarios WHERE nombre_inventario = %s", (inventario,))
            id_inventario = cursor.fetchone()[0]

            cursor.execute("""
                INSERT INTO productos (nombre_producto, descripcion, precio, codigo_barras, id_categoria, id_marca, id_proveedor)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (nombre, descripcion, precio, codigo_barras, id_categoria, id_marca, id_proveedor))

            id_producto = cursor.lastrowid

            if inventario == "Ventas":
                cursor.execute("""
                    INSERT INTO inventario_producto (id_producto, id_inventario, cantidad, porcentaje_operacion)
                    VALUES (%s, %s, %s, %s)
                """, (id_producto, id_inventario, cantidad, porcentaje_operacion))
            else:
                cursor.execute("""
                    INSERT INTO inventario_interno (id_producto, id_inventario_interno, id_inventario, cantidad, porcentaje_operacion)
                    VALUES (%s, %s, %s, %s, %s)
                """, (id_producto, id_inventario, id_inventario, cantidad, porcentaje_operacion))

            self.db_connection.commit()
            QMessageBox.information(
                self, "Éxito", "Producto agregado exitosamente.")
            # Actualizar la tabla de productos en la ventana principal
            self.main_window.load_products_table()
            self.close()
        except mysql.connector.Error as err:
            print(f"Error al agregar el producto: {err}")
            QMessageBox.warning(
                self, "Error", f"Error al agregar el producto: {err}")

    def add_category(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Agregar Categoría")
        layout = QVBoxLayout(dialog)
        category_input = QLineEdit(dialog)
        layout.addWidget(QLabel("Nombre de la categoría:", dialog))
        layout.addWidget(category_input)
        button = QPushButton("Agregar", dialog)
        layout.addWidget(button)

        def on_add_category():
            category_name = category_input.text()
            self.db_connection = check_connection(self.db_connection)
            try:
                cursor = self.db_connection.cursor()
                cursor.execute(
                    "INSERT INTO categorias (nombre_categoria) VALUES (%s)", (category_name,))
                self.db_connection.commit()
                self.ui.categoriaInput.addItem(category_name)
                dialog.accept()
            except mysql.connector.Error as err:
                print("Error al agregar la categoría:", err)
                QMessageBox.warning(
                    self, "Error", f"Error al agregar la categoría: {err}")

        button.clicked.connect(on_add_category)
        dialog.exec_()

    def add_brand(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Agregar Marca")
        layout = QVBoxLayout(dialog)
        brand_input = QLineEdit(dialog)
        layout.addWidget(QLabel("Nombre de la marca:", dialog))
        layout.addWidget(brand_input)
        button = QPushButton("Agregar", dialog)
        layout.addWidget(button)

        def on_add_brand():
            brand_name = brand_input.text()
            self.db_connection = check_connection(self.db_connection)
            try:
                cursor = self.db_connection.cursor()
                cursor.execute(
                    "INSERT INTO marcas (nombre_marca) VALUES (%s)", (brand_name,))
                self.db_connection.commit()
                self.ui.marcaInput.addItem(brand_name)
                dialog.accept()
            except mysql.connector.Error as err:
                print("Error al agregar la marca:", err)
                QMessageBox.warning(
                    self, "Error", f"Error al agregar la marca: {err}")

        button.clicked.connect(on_add_brand)
        dialog.exec_()

    def add_supplier(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Agregar Proveedor")
        layout = QVBoxLayout(dialog)
        supplier_input = QLineEdit(dialog)
        layout.addWidget(QLabel("Nombre del proveedor:", dialog))
        layout.addWidget(supplier_input)
        button = QPushButton("Agregar", dialog)
        layout.addWidget(button)

        def on_add_supplier():
            supplier_name = supplier_input.text()
            self.db_connection = check_connection(self.db_connection)
            try:
                cursor = self.db_connection.cursor()
                cursor.execute(
                    "INSERT INTO proveedores (nombre_proveedor) VALUES (%s)", (supplier_name,))
                self.db_connection.commit()
                self.ui.proveedorInput.addItem(supplier_name)
                dialog.accept()
            except mysql.connector.Error as err:
                print("Error al agregar el proveedor:", err)
                QMessageBox.warning(
                    self, "Error", f"Error al agregar el proveedor: {err}")

        button.clicked.connect(on_add_supplier)
        dialog.exec_()

    def closeEvent(self, event):
        try:
            close_connection(self.db_connection)
        except Exception as e:
            print("Error al cerrar la conexión de la base de datos:", e)
        event.accept()
