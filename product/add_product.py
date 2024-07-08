from PySide6.QtWidgets import QMainWindow, QMessageBox, QInputDialog
from product.add_product_ui import Ui_AddProductWindow
from database.database import create_connection, close_connection
import mysql.connector


class AddProductWindow(QMainWindow):
    def __init__(self, codigo_barras):
        super(AddProductWindow, self).__init__()
        self.ui = Ui_AddProductWindow()
        self.ui.setupUi(self)
        self.ui.codigoBarrasInput.setText(codigo_barras)
        self.ui.agregarButton.clicked.connect(self.add_product)
        self.ui.categoriaButton.clicked.connect(self.add_category)
        self.ui.marcaButton.clicked.connect(self.add_brand)
        self.ui.ProveedorButton.clicked.connect(self.add_supplier)
        self.populate_combo_boxes()

    def populate_combo_boxes(self):
        conn = None
        try:
            conn = create_connection()
            cursor = conn.cursor()

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
            print(f"Error al poblar los desplegables: {err}")
        finally:
            if conn:
                close_connection(conn)

    def add_category(self):
        category, ok = QInputDialog.getText(
            self, 'Nueva Categoría', 'Ingrese el nombre de la nueva categoría:')
        if ok and category:
            conn = None
            try:
                conn = create_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO categorias (nombre_categoria) VALUES (%s)", (category,))
                conn.commit()
                self.ui.categoriaInput.addItem(category)
            except mysql.connector.Error as err:
                QMessageBox.warning(
                    self, "Error", f"Error al agregar la categoría: {err}")
            finally:
                if conn:
                    close_connection(conn)

    def add_brand(self):
        brand, ok = QInputDialog.getText(
            self, 'Nueva Marca', 'Ingrese el nombre de la nueva marca:')
        if ok and brand:
            conn = None
            try:
                conn = create_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO marcas (nombre_marca) VALUES (%s)", (brand,))
                conn.commit()
                self.ui.marcaInput.addItem(brand)
            except mysql.connector.Error as err:
                QMessageBox.warning(
                    self, "Error", f"Error al agregar la marca: {err}")
            finally:
                if conn:
                    close_connection(conn)

    def add_supplier(self):
        supplier, ok = QInputDialog.getText(
            self, 'Nuevo Proveedor', 'Ingrese el nombre del nuevo proveedor:')
        if ok and supplier:
            conn = None
            try:
                conn = create_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO proveedores (nombre_proveedor) VALUES (%s)", (supplier,))
                conn.commit()
                self.ui.proveedorInput.addItem(supplier)
            except mysql.connector.Error as err:
                QMessageBox.warning(
                    self, "Error", f"Error al agregar el proveedor: {err}")
            finally:
                if conn:
                    close_connection(conn)

    def add_product(self):
        nombre = self.ui.nombreInput.text()
        inventario = self.ui.inventarioInput.currentText()
        precio = self.ui.precioInput.text()
        descripcion = self.ui.descripcionInput.text()
        codigo_barras = self.ui.codigoBarrasInput.text()
        categoria = self.ui.categoriaInput.currentText()
        marca = self.ui.marcaInput.currentText()
        proveedor = self.ui.proveedorInput.currentText()
        cantidad = self.ui.cantidadInput.value()
        porcentaje_operacion = self.ui.porcentajeOperacionInput.text()

        if not nombre or not inventario or not precio or not descripcion or not codigo_barras or not categoria or not marca or not proveedor:
            QMessageBox.warning(
                self, "Error", "Por favor, complete todos los campos.")
            return

        conn = None
        try:
            conn = create_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT id_categoria FROM categorias WHERE nombre_categoria=%s", (categoria,))
            id_categoria = cursor.fetchone()[0]

            cursor.execute(
                "SELECT id_marca FROM marcas WHERE nombre_marca=%s", (marca,))
            id_marca = cursor.fetchone()[0]

            cursor.execute(
                "SELECT id_proveedor FROM proveedores WHERE nombre_proveedor=%s", (proveedor,))
            id_proveedor = cursor.fetchone()[0]

            cursor.execute("INSERT INTO productos (nombre_producto, descripcion, precio, codigo_barras, id_categoria, id_marca, id_proveedor) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (nombre, descripcion, precio, codigo_barras, id_categoria, id_marca, id_proveedor))
            conn.commit()

            cursor.execute(
                "SELECT id_producto FROM productos WHERE codigo_barras=%s", (codigo_barras,))
            id_producto = cursor.fetchone()[0]

            cursor.execute(
                "SELECT id_inventario FROM inventarios WHERE nombre_inventario=%s", (inventario,))
            id_inventario = cursor.fetchone()[0]

            cursor.execute("INSERT INTO inventario_producto (id_inventario, id_producto, cantidad, porcentaje_operacion) VALUES (%s, %s, %s, %s)",
                           (id_inventario, id_producto, cantidad, porcentaje_operacion))
            conn.commit()

            QMessageBox.information(
                self, "Éxito", "Producto agregado exitosamente.")
            self.close()

        except mysql.connector.Error as err:
            print(f"Error al agregar el producto: {err}")
            QMessageBox.warning(
                self, "Error", f"Error al agregar el producto: {err}")
        finally:
            if conn:
                close_connection(conn)
