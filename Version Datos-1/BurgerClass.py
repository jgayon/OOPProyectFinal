import pandas as pd

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def esta_vacia(self):
        return self.head is None

    def append(self, data):
        new_node = Nodo(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def agregar(self, ingrediente):
        nuevo_nodo = Nodo(ingrediente)
        if self.esta_vacia():
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo
    
    def obtener_elementos(self):
        elementos = []
        current = self.head
        while current is not None:
            elementos.append(current.data)
            current = current.next
        return elementos

class Ingrediente:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Hamburguesa:
    def __init__(self):
        self.ingredientes = ListaEnlazada()

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.agregar(ingrediente)

    def remover_ingrediente(self, ingrediente):
        current = self.ingredientes.head
        prev = None
        while current is not None:
            if current.data == ingrediente:
                if prev is None:
                    self.ingredientes.head = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
    def obtener_ingredientes(self):
        ingredientes = []
        current = self.ingredientes.head
        while current is not None:
            ingredientes.append(current.data)
            current = current.next
        return ingredientes

    def calcular_precio(self):
        precio_total = 0
        current = self.ingredientes.head
        while current is not None:
            ingrediente = current.data
            precio_total += ingrediente.precio
            current = current.next
        return precio_total
    def obtener_ingredientes(self):
        ingredientes = []
        current = self.ingredientes.head
        while current is not None:
            ingrediente = current.data
            ingredientes.append(ingrediente)
            current = current.next
        return ingredientes

class Tienda:
    def __init__(self):
        self.ingredientes_disponibles = []

    def cargar_ingredientes(self):
        df = pd.read_excel('Version Datos-1/Ingredientes.xlsx')
        for index, row in df.iterrows():
            nombre = row['Nombre']
            precio = row['Precio']
            ingrediente = Ingrediente(nombre, precio)
            self.ingredientes_disponibles.append(ingrediente)

    def mostrar_ingredientes_disponibles(self):
        for ingrediente in self.ingredientes_disponibles:
            print(ingrediente.nombre, ingrediente.precio)

    def obtener_ingrediente_por_nombre(self, nombre):
        for ingrediente in self.ingredientes_disponibles:
            if ingrediente.nombre.lower() == nombre.lower():
                return ingrediente
        return None

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hamburguesa = Hamburguesa()
        self.ingredientes_seleccionados = []

    def armar_hamburguesa(self, tienda, ingrediente):
        if ingrediente in self.ingredientes_seleccionados:
            self.ingredientes_seleccionados.remove(ingrediente)
            self.hamburguesa.remover_ingrediente(ingrediente)
        else:
            self.ingredientes_seleccionados.append(ingrediente)
            self.hamburguesa.agregar_ingrediente(ingrediente)

    def deshacer_seleccion(self):
        if self.ingredientes_seleccionados:
            ultimo_ingrediente = self.ingredientes_seleccionados.pop()
            self.hamburguesa.remover_ingrediente(ultimo_ingrediente)

    def finalizar_hamburguesa(self):
        if self.ingredientes_seleccionados:
            self.ingredientes_seleccionados = []
            self.hamburguesa = Hamburguesa()

    def mostrar_resumen(self):
        print("Hamburguesa de", self.nombre)
        print("Ingredientes seleccionados:")
        for ingrediente in self.hamburguesa.obtener_ingredientes():
            print(ingrediente.nombre, ingrediente.precio)
        print("Total:", self.hamburguesa.calcular_precio())

    def hamburguesa_contiene_ingrediente(self, nombre_ingrediente):
        for ingrediente in self.ingredientes_seleccionados:
            if ingrediente.nombre.lower() == nombre_ingrediente.lower():
                return True
        return False
    
    def mostrar_cuenta(self):
        print("Resumen de la hamburguesa:")
        print("Ingredientes:")
        ingredientes = self.hamburguesa.ingredientes.obtener_elementos()
        for ingrediente in ingredientes:
            print(f"- {ingrediente.nombre} (${ingrediente.precio})")
        print(f"Total a pagar: ${self.hamburguesa.calcular_precio()}")