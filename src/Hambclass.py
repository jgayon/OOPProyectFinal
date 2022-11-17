import Escoger

"""
Clases de Ingredientes + Bebidas. Son Polimorphas, y  contienen el metodo de seleccion de
los ingredientes etc.
"""
#clase bebida
class Bebida:
    menu =['Coca Cola','Pepsi','Kola Roman','Sprite']
    #metodos bebida
    def __init__(self,bebidaesc,costb) -> None:
        self.bebidaesc = bebidaesc
        self.costb= costb
    bebida = {
        'Coca Cola':3500,
        'Pepsi':3000,
        'Kola Roman':2500,
        'Sprite':2500
    }
    
    def escoger_bebida():
        sw= input('Quiere añadir una bebida a su pedido? Si o No\n')
        Bebida.bebidaesc= []
        
        if sw == 'Si':
            print('---Bebidas---\n')
            cont= True
            Bebida.costb = 0
            while cont == True:
                selec = Escoger.escoger(Bebida.menu)
                Bebida.bebidaesc.append(selec)
                Bebida.costb = Bebida.costb + Bebida.bebida[selec]
                contpreg= input('Quiere añadir otra? Si o No\n')
                if contpreg == 'No':
                    cont = False
                else:
                    cont = True
        elif sw == 'No':
            Bebida.costb = 0
#clase pan
class Pan:
    menu=['Blanco','Integral','Oregano']
    #metodos pan
    def __init__(self,panesc='',costp=0) -> None:
        self.panesc = panesc
        self.costp = costp
    pan = {
        'Blanco':2000,
        'Integral':2500,
        'Oregano':2700
    }
    def escoger_pan():
        print('---Pan---\n')
        selec = Escoger.escoger(Pan.menu)
        Pan.panesc = selec
        Pan.costp = Pan.pan[selec]
        
#clase queso
class Queso:
    menu=['Americano','Cheddar','Mozzarella','Provolone']
    #metodos queso
    def __init__(self,quesoesc='',costq=0) -> None:
        self.quesoesc = quesoesc
        self.costq = costq
    queso = {
        'Americano':500,
        'Cheddar':500,
        'Mozzarella':500,
        'Provolone':500        
    }
    def escoger_queso():
        print('---Quesos---\n')
        cont = True
        Queso.quesoesc= []
        Queso.costq = 0
        while cont == True:
            selec= Escoger.escoger(Queso.menu)
            Queso.quesoesc.append(selec)
            Queso.costq = Queso.costq + Queso.queso[selec]
            contpreg= input('\nQuiere añadir otra? Si o No\n')
            if contpreg == 'No':
                cont = False
            else:
                cont = True
#clase carne
class Carne:
    menu=['Carne','Pollo','Doble Carne','Doble Pollo','Carne Pollo']
    #metodos carne
    def __init__(self,carnesc='',costc=0) -> None:
        self.carnesc = carnesc
        self.costc = costc
    carne={
        'Carne':8000,
        'Pollo':8000,
        'Doble Carne':9500,
        'Doble Pollo':9500,
        'Carne Pollo':10000

    }
    def escoger_carne():
        print('---Proteinas---\n')
        selec = Escoger.escoger(Carne.menu)
        Carne.carnesc = selec
        Carne.costc = Carne.carne[selec]
            
#clase salsa
class Salsa:
    menu = ['Tomate','Mayonesa',
        'Cebolla dulce',
        'Picante']
    #metodos salsa
    def __init__(self,salsaesc='',costs=0) -> None:
        self.salsaesc = salsaesc
        self.costs = costs
    salsa = {
        'Tomate':200,
        'Mayonesa':200,
        'Cebolla dulce':250,
        'Picante':250
    }
    def escoger_salsa():
        print('---Salsas---\n')
        cont = True
        Salsa.salsaesc= []
        Salsa.costs = 0
        while cont == True:
            selec= Escoger.escoger(Salsa.menu)
            Salsa.salsaesc.append(selec)
            Salsa.costs = Salsa.costs + Salsa.salsa[selec]
            contpreg= input('\nQuiere añadir otra? Si o No\n')
            if contpreg == 'No':
                cont = False
            else:
                cont = True
#clase verdura
class Verdura:
    menu=['Cebolla', 'Lechuga', 'Tomate', 'Pepinillos']
    #metodos verdura
    def __init__(self,verduraesc='',costv=0) -> None:
        self.verduraesc = verduraesc
        self.costv = costv
    verdura={
        'Cebolla':200,
        'Lechuga':200,
        'Tomate':200,
        'Pepinillos':200
    }
    def escoger_verdura():
        print('---Verduras---\n')
        cont = True
        Verdura.verduraesc= []
        Verdura.costv = 0
        while cont == True:
            
            selec= Escoger.escoger(Verdura.menu)
            Verdura.verduraesc.append(selec)
            Verdura.costv = Verdura.costv + Verdura.verdura[selec]
            contpreg= input('\nQuiere añadir otra? Si o No\n')
            if contpreg == 'No':
                cont = False
            else:
                cont = True




"""
Metodo Hamburger: Arma la Hamburguesa.
"""
def hamburger(panesc,carnesc,quesoesc,salsaesc,verduraesc) ->str:
    orderques = (', '.join(Queso.quesoesc))
    ordersals = (', '.join(Salsa.salsaesc))
    orderver = (', '.join(Verdura.verduraesc))
    hamburg = 'Pan '+ panesc +'\n'+ carnesc+'\nQueso(s) ' + orderques +'\ncon salsa(s) de '+ ordersals +'\nY '+ orderver + ' como verduras.'
    print('Su Hamburguesa esta compuesta por {}'.format(hamburg))


"""
Clase Pedido: Contiene todos los metodos de escogencia y el costo final del pedido(balance()). 
Practicamente el codigo principal en si.
"""
class Pedido:
    def __init__(self) -> None:
        self.total_balance = 0

    def pedido():
             
       Pan.escoger_pan()
       Carne.escoger_carne()
       Verdura.escoger_verdura()
       Salsa.escoger_salsa()
       Queso.escoger_queso()
       Bebida.escoger_bebida()
       hamburger(Pan.panesc,Carne.carnesc,Queso.quesoesc,Salsa.salsaesc,Verdura.verduraesc)
       
       

    def balance() -> float:
        Pedido.total_balance = Pedido.total_balance + Carne.costc + Pan.costp + Queso.costq + Salsa.costs + Verdura.costv + Bebida.costb
        return('El valor total de su pedido es: {} pesos.'.format(Pedido.total_balance))

