from BurgerClass import *

# Ejemplo de uso
tienda = Tienda()
tienda.cargar_ingredientes("Ingredientes.xlsx")

cliente = Cliente("Juan")
cliente.armar_hamburguesa(tienda)
cliente.mostrar_cuenta()