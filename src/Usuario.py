from Hambclass import Pedido
from IPython.display import clear_output
'''
Clase Usuario, contiene el metodo de registro del Usuario y el metodo que se encarga de la forma por la cual el usuario va a pagar.
'''

class User():
    
    def __init__(self,nombre,direccion:str,id:int, celular:int, metodop:str) -> None:
        self.direccion = direccion
        self.id = id
        self.celular = celular
        self.metodop = metodop
        self.nombre=nombre
    
    def datos_user():
        clear_output()
        User.nombre= input('Cual es tu Nombre: \n')
        User.direccion = input('Escriba la direccion de su domicilio: \n')
        User.id = int(input('Digite su numero de cedula: \n'))
        User.celular= int(input('Digite su numero de Celular: \n'))
    
    def metodos_pago():
        User.metodop = input('Como planea pagar su compra? Efectivo, Tarjeta o  Aplicacion Bancaria?\n')
        if User.metodop == 'Efectivo':
            print('Ha elegido Pago por Efectivo.')
            print(f'El valor de su pedido es: {Pedido.total_balance}')
            pagare=int(input('Digite el monto que pagara: \n'))
            cambio= pagare - Pedido.total_balance  
            print(f'Tu cambio total es: {cambio}')
        elif User.metodop == 'Tarjeta':
            print('Ha elegido pago por Tarjeta.')
            tarjeta=input('Digite el numero de su Tarjeta: \n')
            print('Procesando...')
            print(f'Transaccion Aprobada!\nSe han transferido {Pedido.total_balance} pesos.')
        elif User.metodop == 'Aplicacion Bancaria':
            print('Ha elegido Pago por Aplicacion Bancaria.')
            banco=input('Digite el Banco por cual va a pagar: \n')
            cuenta= input('Ingrese el numero de cuenta: \n')
            print('Procesando...')
            print(f'Transaccion Aprobada!\nSe han transferido {Pedido.total_balance} pesos de la {cuenta} del Banco {banco}.')
        print(f'Muchas gracias por tu compra {User.nombre} tu predido sera entregado a {User.direccion} en momentos!')

