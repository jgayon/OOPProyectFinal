import pandas as pd


class Ingrediente:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Hamburguesa:
    def __init__(self):
        self.ingredientes = []

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def calcular_precio(self):
        total = 0
        for ingrediente in self.ingredientes:
            total += ingrediente.precio
        return total

class Tienda:
    def __init__(self):
        self.ingredientes_disponibles = []

    def cargar_ingredientes(self, archivo):
        df = pd.read_excel(archivo)
        for index, row in df.iterrows():
            nombre = row['Nombre']
            precio = row['Precio']
            ingrediente = Ingrediente(nombre, precio)
            self.ingredientes_disponibles.append(ingrediente)

    def mostrar_ingredientes_disponibles(self):
        for ingrediente in self.ingredientes_disponibles:
            print(ingrediente.nombre, ingrediente.precio)

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hamburguesa = None

    def armar_hamburguesa(self, tienda):
        self.hamburguesa = Hamburguesa()
        tienda.mostrar_ingredientes_disponibles()

        while True:
            opcion = input("Seleccione un ingrediente (o 'salir' para finalizar): ")
            if opcion == "salir":
                break

            ingrediente = tienda.obtener_ingrediente(opcion)
            if ingrediente:
                self.hamburguesa.agregar_ingrediente(ingrediente)
            else:
                print("Ingrediente no válido.")

    def mostrar_cuenta(self):
        print("Hamburguesa de", self.nombre)
        print("Ingredientes:")
        for ingrediente in self.hamburguesa.ingredientes:
            print(ingrediente.nombre, ingrediente.precio)
        print("Total:", self.hamburguesa.calcular_precio())