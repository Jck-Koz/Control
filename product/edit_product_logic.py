import mysql.connector
from PySide6.QtWidgets import QMainWindow, QMessageBox, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel
from .editprod import Ui_EditProductWindow
from database.database import create_connection, close_connection, check_connection
from datetime import datetime


class EditProductLogic(QMainWindow):
    def __init__(self, product_id, main_window):
        super(EditProductLogic, self).__init__()
        self.ui = Ui_EditProductWindow()
        self.ui.setupUi(self)
        self.db_connection = create_connection()
        self.main_window = main_window  # Referencia a la ventana principal
        self.product_id = product_id
        # Id del usuario que está realizando la operación
        self.user_id = main_window.user_id
        self.populate_comboboxes()
        self.load_product_details()

        self.ui.categoriaButton.clicked.connect(self.add_category)
        self.ui.marcaButton.clicked.connect(self.add_brand)
        self.ui.ProveedorButton.clicked.connect(self.add_supplier)
        self.ui.EntradaButton.clicked.connect(self.update_inventory_entry)
        self.ui.salidaButton.clicked.connect(self.update_inventory_exit)

    def populate_comboboxes(self):
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

    def load_product_details(self):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT p.nombre_producto, p.descripcion, p.precio, p.codigo_barras, c.nombre_categoria, m.nombre_marca, 
                       pr.nombre_proveedor, COALESCE(ip.cantidad, 0), COALESCE(ip.porcentaje_operacion, 0), COALESCE(i.nombre_inventario, '')
                FROM productos p
                JOIN categorias c ON p.id_categoria = c.id_categoria
                JOIN marcas m ON p.id_marca = m.id_marca
                JOIN proveedores pr ON p.id_proveedor = pr.id_proveedor
                LEFT JOIN inventario_producto ip ON p.id_producto = ip.id_producto
                LEFT JOIN inventarios i ON ip.id_inventario = i.id_inventario
                WHERE p.id_producto = %s
            """, (self.product_id,))
            product = cursor.fetchone()
            if not product:
                cursor.execute("""
                    SELECT p.nombre_producto, p.descripcion, p.precio, p.codigo_barras, c.nombre_categoria, m.nombre_marca, 
                           pr.nombre_proveedor, COALESCE(ii.cantidad, 0), COALESCE(ii.porcentaje_operacion, 0), COALESCE(i.nombre_inventario, '')
                    FROM productos p
                    JOIN categorias c ON p.id_categoria = c.id_categoria
                    JOIN marcas m ON p.id_marca = m.id_marca
                    JOIN proveedores pr ON p.id_proveedor = pr.id_proveedor
                    LEFT JOIN inventario_interno ii ON p.id_producto = ii.id_producto
                    LEFT JOIN inventarios i ON ii.id_inventario = i.id_inventario
                    WHERE p.id_producto = %s
                """, (self.product_id,))
                product = cursor.fetchone()

            if product:
                self.ui.nombreInput.setText(product[0])
                self.ui.descripcionInput.setText(product[1])
                self.ui.precioInput.setText(str(product[2]))
                self.ui.codigoBarrasInput.setText(product[3])
                self.ui.categoriaInput.setCurrentText(product[4])
                self.ui.marcaInput.setCurrentText(product[5])
                self.ui.proveedorInput.setCurrentText(product[6])
                # Mostrar siempre 1 en la interfaz
                self.ui.cantidadInput.setValue(1)
                self.ui.porcentajeOperacionInput.setText(
                    str(product[8]) if product[8] is not None else '0.0')
                self.ui.inventarioInput.setCurrentText(product[9])
            else:
                QMessageBox.warning(self, "Error", "Producto no encontrado.")
        except mysql.connector.Error as err:
            print("Error al cargar los detalles del producto:", err)
            QMessageBox.warning(
                self, "Error", f"Error al cargar los detalles del producto: {err}")

    def update_inventory_entry(self):
        try:
            cantidad = self.ui.cantidadInput.value()
            id_inventario = self.get_inventario_id()
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT cantidad FROM inventario_producto WHERE id_producto = %s AND id_inventario = %s",
                           (self.product_id, id_inventario))
            stock = cursor.fetchone()
            if stock:
                nueva_cantidad = stock[0] + cantidad
                cursor.execute("UPDATE inventario_producto SET cantidad = %s WHERE id_producto = %s AND id_inventario = %s",
                               (nueva_cantidad, self.product_id, id_inventario))
            else:
                cursor.execute("""
                    INSERT INTO inventario_producto (id_inventario, id_producto, cantidad, porcentaje_operacion)
                    VALUES (%s, %s, %s, %s)
                """, (id_inventario, self.product_id, cantidad, float(self.ui.porcentajeOperacionInput.text())))
            self.db_connection.commit()
            cursor.execute("""
                INSERT INTO ventas (id_producto, id_usuario, cantidad, porcentaje_venta, fecha_venta, id_inventario, tipo)
                VALUES (%s, %s, %s, %s, %s, %s, 'entrada')
            """, (self.product_id, self.user_id, cantidad, float(self.ui.porcentajeOperacionInput.text()),
                  datetime.now().strftime("%Y-%m-%d %H:%M:%S"), id_inventario))
            self.db_connection.commit()
            # Actualizar la tabla de productos en la ventana principal
            self.main_window.load_products_table()
            self.main_window.load_combined_sales_table()
            QMessageBox.information(
                self, "Éxito", "Entrada de inventario actualizada exitosamente.")
        except mysql.connector.Error as err:
            print("Error al actualizar la entrada de inventario:", err)
            QMessageBox.warning(
                self, "Error", f"Error al actualizar la entrada de inventario: {err}")

    def update_inventory_exit(self):
        try:
            cantidad = self.ui.cantidadInput.value()
            id_inventario = self.get_inventario_id()
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT cantidad FROM inventario_producto WHERE id_producto = %s AND id_inventario = %s",
                           (self.product_id, id_inventario))
            stock = cursor.fetchone()
            if stock and stock[0] >= cantidad:
                nueva_cantidad = stock[0] - cantidad
                cursor.execute("UPDATE inventario_producto SET cantidad = %s WHERE id_producto = %s AND id_inventario = %s",
                               (nueva_cantidad, self.product_id, id_inventario))
                self.db_connection.commit()
                cursor.execute("""
                    INSERT INTO ventas (id_producto, id_usuario, cantidad, porcentaje_venta, fecha_venta, id_inventario, tipo)
                    VALUES (%s, %s, %s, %s, %s, %s, 'salida')
                """, (self.product_id, self.user_id, cantidad, float(self.ui.porcentajeOperacionInput.text()),
                      datetime.now().strftime("%Y-%m-%d %H:%M:%S"), id_inventario))
                self.db_connection.commit()
                # Actualizar la tabla de productos en la ventana principal
                self.main_window.load_products_table()
                self.main_window.load_combined_sales_table()
                QMessageBox.information(
                    self, "Éxito", "Salida de inventario actualizada exitosamente.")
            else:
                QMessageBox.warning(
                    self, "Error", "Stock insuficiente para realizar la salida.")
        except mysql.connector.Error as err:
            print("Error al actualizar la salida de inventario:", err)
            QMessageBox.warning(
                self, "Error", f"Error al actualizar la salida de inventario: {err}")

    def get_inventario_id(self):
        cursor = self.db_connection.cursor()
        cursor.execute(
            "SELECT id_inventario FROM inventarios WHERE nombre_inventario = %s", (self.ui.inventarioInput.currentText(),))
        result = cursor.fetchone()
        return result[0] if result else None

    def add_category(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Agregar Categoría")
        layout = QVBoxLayout(dialog)
        label = QLabel("Nombre de la nueva categoría:")
        layout.addWidget(label)
        category_input = QLineEdit()
        layout.addWidget(category_input)
        button = QPushButton("Agregar")
        layout.addWidget(button)

        def on_add_category():
            category_name = category_input.text()
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
        label = QLabel("Nombre de la nueva marca:")
        layout.addWidget(label)
        brand_input = QLineEdit()
        layout.addWidget(brand_input)
        button = QPushButton("Agregar")
        layout.addWidget(button)

        def on_add_brand():
            brand_name = brand_input.text()
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
        label = QLabel("Nombre del nuevo proveedor:")
        layout.addWidget(label)
        supplier_input = QLineEdit()
        layout.addWidget(supplier_input)
        button = QPushButton("Agregar")
        layout.addWidget(button)

        def on_add_supplier():
            supplier_name = supplier_input.text()
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
            print("Database connection closed.")
        except Exception as e:
            print("Error al cerrar la conexión de la base de datos:", e)
        event.accept()
