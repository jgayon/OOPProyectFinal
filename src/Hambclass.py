
from ast import Break


class Usuario:
    def __init__(self,direccion:str,id:int, celular:int, metodop:str) -> None:
        self.direccion = direccion
        self.id = id
        self.celular = celular
        self.metodop = metodop
    
    def datos_user():
        Usuario.direccion = input('Escriba la direccion de su domicilio: \n')
        Usuario.id = int(input('Digite su numero de cedula: \n'))
        Usuario.celular= int(input('Digite su numero de Celular: \n'))
    def metodos_pago():
        Usuario.metodop = input('Como planea pagar su compra? Efectivo, Tarjeta o  Aplicacion Bancaria?\n')
        if Usuario.metodop == 'Efectivo':
            pass
        elif Usuario.metodop == 'Tarjeta':
            pass
        elif Usuario.metodop == 'Aplicacion Bancaria':
            pass

class Bebida:
    def __init__(self,bebidaesc,costb) -> None:
        self.bebidaesc = bebidaesc
        self.costob= costb
    bebida = {
        'Coca Cola':['Coca Cola',3500],
        'Pepsi':['Pepsi',3000],
        'Kola Roman':['Kola Roman',2500],
        'Sprite':['Sprite',2500]
    }
    def escoger_bebida():
        sw= input('Quiere añadir una bebida a su pedido? Si o No\n')
        if sw == 'Si':
            print('Estos son nuestras Bebidas: ')
            print(Bebida.bebida.keys())
            selec=input('Cual desea?\n')
            Bebida.bebidaesc = Bebida.bebida[selec][0]
            Bebida.costb = Bebida.bebida[selec][1]
        elif sw == 'No':
            Bebida.costb = 0

class Pan:
    def __init__(self,panesc='',costp=0) -> None:
        self.panesc = panesc
        self.costp = costp
    pan = {
        'Blanco':['Blanco',2000],
        'Integral':['Integral', 2500],
        'Oregano':['Oregano',2700],
    }
    def escoger_pan():
        print('Estos son nuestros Panes: ')
        print(Pan.pan.keys())
        selec=input('Que pan prefiere?\n')
        Pan.panesc = Pan.pan[selec][0]
        Pan.costp = Pan.pan[selec][1]

class Queso:
    def __init__(self,quesoesc='',costq=0) -> None:
        self.quesoesc = quesoesc
        self.costq = costq
    queso = {
        'Americano':['Americano',500],
        'Cheddar':['Cheddar',500],
        'Mozzarella':['Mozzarella',500],
        
    }
    def escoger_queso():
        print('Estos son nuestros Quesos: ')
        print(Queso.queso.keys())
        selec=input('Cual queso prefiere?\n')
        Queso.quesoesc = Queso.queso[selec][0]
        Queso.costq = Queso.queso[selec][1]
class Carne:
    def __init__(self,carnesc='',costc=0) -> None:
        self.carnesc = carnesc
        self.costc = costc
    carne={
        'Carne':['Carne',8000],
        'Pollo':['Pollo',8000],
        'Doble Carne':['Doble Carne',9500],
        'Doble Pollo':['Doble Pollo',9500],
        'Carne Pollo':['Carne + Pollo',10000]

    }
    def escoger_carne():
        print('Estos son nuestras Proteinas: ')
        print(Carne.carne.keys())
        selec=input('Que Proteina prefiere?\n')
        Carne.carnesc = Carne.carne[selec][0]
        Carne.costc = Carne.carne[selec][1]
class Salsa:
    def __init__(self,salsaesc='',costs=0) -> None:
        self.salsaesc = salsaesc
        self.costs = costs
    salsa = {
        'Tomate':['Tomate',200],
        'Mayonesa':['Mayonesa',200],
        'Cebolla Dulce':['Cebolla Dulce',250],
        'Picante':['Picante',250]
    }
    def escoger_salsa():
        print('Estos son nuestras Salsas: ')
        print(Salsa.salsa.keys())
        selec=input('Que Salsa le quiere poner?\n')
        Salsa.salsaesc = Salsa.salsa[selec][0]
        Salsa.costs = Salsa.salsa[selec][1]
class Verdura:
    def __init__(self,verduraesc='',costv=0) -> None:
        self.verduraesc = verduraesc
        self.costv = costv
    verdura={
        'Cebolla':['Cebolla',200],
        'Lechuga':['Lechuga',200],
        'Tomate':['Tomate',200],
        'Pepinillos':['Pepinillos',200]
    }
    def escoger_verdura():
        print('Estos son nuestras Verduras: ')
        print(Verdura.verdura.keys())
        selec=input('Que Verdura quiere añadir?\n')
        Verdura.verduraesc = Verdura.verdura[selec][0]
        Verdura.costv = Verdura.verdura[selec][1]

def hamburger(panesc,carnesc,quesoesc,salsaesc,verduraesc) ->str:
        hamburg = 'Pan '+ panesc +', '+ carnesc+', queso ' + quesoesc +', con salsa de '+ salsaesc +' y '+ verduraesc
        print('Su Hamburguesa esta compuesta por {}'.format(hamburg))

class Pedido:
    def pedido():
             
       Pan.escoger_pan()
       Carne.escoger_carne()
       Verdura.escoger_verdura()
       Salsa.escoger_salsa()
       Queso.escoger_queso()
       hamburger(Pan.panesc,Carne.carnesc,Queso.quesoesc,Salsa.salsaesc,Verdura.verduraesc)
       Bebida.escoger_bebida()
       

    def balance() -> float:
        total_balance = Carne.costc + Pan.costp + Queso.costq + Salsa.costs + Verdura.costv + Bebida.costb
        print('El valor total de su pedido es: {} pesos.'.format(total_balance))
