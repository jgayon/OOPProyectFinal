import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout,
                              QWidget, QPushButton, QMessageBox, QDialog, QVBoxLayout, 
                              QLineEdit, QComboBox)

# Importar las clases existentes
from BurgerClass import Tienda, Cliente, Ingrediente, Hamburguesa, ListaEnlazada

class PagoDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pago")
        self.setGeometry(200, 200, 300, 200)

        # Crear elementos de la GUI
        self.label_nombre = QLabel("Nombre:")
        self.line_edit_nombre = QLineEdit()

        self.label_direccion = QLabel("Dirección:")
        self.line_edit_direccion = QLineEdit()

        self.label_cedula = QLabel("Cédula:")
        self.line_edit_cedula = QLineEdit()

        self.label_metodo_pago = QLabel("Método de Pago:")
        self.combo_box_metodo_pago = QComboBox()
        self.combo_box_metodo_pago.addItem("Efectivo")
        self.combo_box_metodo_pago.addItem("Tarjeta de Crédito")
        self.combo_box_metodo_pago.addItem("Transferencia Bancaria")

        self.btn_pagar = QPushButton("Pagar")
        self.btn_pagar.clicked.connect(self.realizar_pago)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_nombre)
        self.layout.addWidget(self.line_edit_nombre)
        self.layout.addWidget(self.label_direccion)
        self.layout.addWidget(self.line_edit_direccion)
        self.layout.addWidget(self.label_cedula)
        self.layout.addWidget(self.line_edit_cedula)
        self.layout.addWidget(self.label_metodo_pago)
        self.layout.addWidget(self.combo_box_metodo_pago)
        self.layout.addWidget(self.btn_pagar)

        self.setLayout(self.layout)

    def realizar_pago(self):
        nombre = self.line_edit_nombre.text()
        direccion = self.line_edit_direccion.text()
        cedula = self.line_edit_cedula.text()
        metodo_pago = self.combo_box_metodo_pago.currentText()

        mensaje = f"¡Pago realizado!\n\nNombre: {nombre}\nDirección: {direccion}\nCédula: {cedula}\nMétodo de Pago: {metodo_pago}"
        QMessageBox.information(self, "Pago", mensaje)

        self.close()

class ResumenCuentaDialog(QDialog):
    def __init__(self, cliente):
        super().__init__()

        self.setWindowTitle("Resumen de la cuenta")
        self.setGeometry(200, 200, 300, 200)

        # Crear elementos de la GUI
        self.label_resumen = QLabel()
        self.label_total = QLabel()

        self.btn_pagar = QPushButton("Pagar")
        self.btn_pagar.clicked.connect(self.realizar_pago)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_resumen)
        self.layout.addWidget(self.label_total)
        self.layout.addWidget(self.btn_pagar)

        self.setLayout(self.layout)

        # Mostrar el resumen de la cuenta
        self.mostrar_resumen_cuenta(cliente)

    def mostrar_resumen_cuenta(self, cliente):
        resumen = "Resumen de la hamburguesa:\n\n"
        ingredientes = cliente.hamburguesa.obtener_ingredientes()
        for ingrediente in ingredientes:
            resumen += f"- {ingrediente.nombre} (${ingrediente.precio})\n"

        total = f"Total a pagar: ${cliente.hamburguesa.calcular_precio()}"

        self.label_resumen.setText(resumen)
        self.label_total.setText(total)

    def realizar_pago(self):
        dialog = PagoDialog()
        dialog.exec_()

class MainWindow(QMainWindow):
    def __init__(self, tienda):
        super().__init__()

        self.setWindowTitle("Armar Hamburguesa")
        self.setGeometry(200, 200, 400, 300)

        # Crear objetos de las clases existentes
        self.tienda = tienda

        self.cliente = Cliente("Cliente")

        # Crear elementos de la GUI
        self.label = QLabel("Seleccione un ingrediente:")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)

        self.btn_ingredientes = []
        for ingrediente in self.tienda.ingredientes_disponibles:
            btn = QPushButton(ingrediente.nombre)
            btn.clicked.connect(lambda checked, i=ingrediente: self.agregar_ingrediente(i))
            self.layout.addWidget(btn)
            self.btn_ingredientes.append(btn)

        self.btn_deshacer = QPushButton("Deshacer selección")
        self.btn_deshacer.clicked.connect(self.deshacer_seleccion)
        self.layout.addWidget(self.btn_deshacer)

        self.btn_finalizar = QPushButton("Finalizar")
        self.btn_finalizar.clicked.connect(self.mostrar_resumen_cuenta)  # Conecta el botón a la función mostrar_resumen_cuenta
        self.layout.addWidget(self.btn_finalizar)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.actualizar_gui()

    def agregar_ingrediente(self, ingrediente):
        self.cliente.armar_hamburguesa(self.tienda, ingrediente)
        self.actualizar_gui()

    def deshacer_seleccion(self):
        self.cliente.deshacer_seleccion()
        self.actualizar_gui()

    def finalizar_hamburguesa(self):
        self.cliente.finalizar_hamburguesa()
        self.mostrar_resumen()

    def actualizar_gui(self):
        for btn in self.btn_ingredientes:
            btn.setEnabled(not self.hamburguesa_contiene_ingrediente(btn.text()))

    def hamburguesa_contiene_ingrediente(self, nombre_ingrediente):
        if not self.cliente.hamburguesa.ingredientes.esta_vacia():
            for ingrediente in self.cliente.hamburguesa.ingredientes.obtener_elementos():
                if ingrediente.nombre.lower() == nombre_ingrediente.lower():
                    return True
        return False

    def mostrar_resumen(self):
        self.cliente.mostrar_resumen()

    def mostrar_resumen_cuenta(self):
        dialog = ResumenCuentaDialog(self.cliente)
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    tienda = Tienda()
    tienda.cargar_ingredientes()

    window = MainWindow(tienda)
    window.show()

    sys.exit(app.exec_())