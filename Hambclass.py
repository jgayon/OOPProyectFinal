
class Usuario:
    pass

class Pan:
    pan = {
        'Blanco':['Blanco',1000],
        'Integral':['Integral', 1000],
        'Oregano':['Oregano',1100],
    }
    def escoger_pan():
        print('Estos son nuestros Panes: ')
        print(Pan.pan.keys())
        selec=input('Que pan prefiere?')
        panesc = Pan.pan[selec][0]
        costp = Pan.pan[selec][1]

class Queso:
    queso = {
        '1':['Americano',300],
        '2':['Cheddar',300],
        '3':['Mozzarella',300],
        
    }
    def escoger_queso():
        print('Estos son nuestros Quesos: ')
        print(Queso.queso.keys())
        selec=input('Cual queso prefiere?')
        quesoesc = Queso.queso[selec][0]
        costq = Queso.queso[selec][1]
class Carne:
    carne={
        '1':['Carne',2000],
        '2':['Pollo',2000],
        '3':['Doble Carne',2500],
        '4':['Doble Pollo',2500],
        '5':['Carne + Pollo',3000]

    }
    def escoger_carne():
        print('Estos son nuestras Proteinas: ')
        print(Carne.carne.keys())
        selec=input('Que Proteina prefiere?')
        carnesc = Carne.carne[selec][0]
        costc = Carne.carne[selec][1]
class Salsa:
    salsa = {
        '1':['Tomate',200],
        '2':['Mayonesa',200],
        '3':['Cebolla Dulce',250],
        '4':['Picante',250]
    }
    def escoger_salsa():
        print('Estos son nuestras Salsas: ')
        print(Salsa.salsa.keys())
        selec=input('Que Salsa le quiere poner?')
        salsaesc = Salsa.salsa[selec][0]
        costs = Salsa.salsa[selec][1]
class Verdura:
    verdura={
        '1':['Cebolla',200],
        '2':['Lechuga',200],
        '3':['Tomate',200],
        '4':['Pepinillos',200]
    }
    def escoger_verdura():
        print('Estos son nuestras Verduras: ')
        print(Verdura.verdura.keys())
        selec=input('Que Verdura quiere añadir?')
        verduraesc = Verdura.verdura[selec][0]
        costv = Verdura.verdura[selec][1]
class Pedido:
    def hamburguesa() -> str:
       def hamburger(panesc:str,carnesc:str,quesoesc:str,salsaesc:str,verduraesc:str) ->str:
        hamburg = panesc + carnesc + quesoesc + salsaesc + verduraesc
        print('Su Hamburguesa esta compuesta por {}'.format(hamburg))

       
       Pan.escoger_pan()
       Carne.escoger_carne()
       Verdura.escoger_verdura()
       Salsa.escoger_salsa()
       Queso.escoger_queso()
       hamburger(Pan.escoger_pan.panesc,Carne.escoger_carne.carnesc,Queso.escoger_queso.quesoesc,Salsa.escoger_salsa.salsaesc,Verdura.escoger_verdura.verduraesc)
       

    def balance(costp:float,costc:float,costq:float,costs:float,costv:float) -> float:
        total_balance = costc + costp + costq + costs + costv
