import Escoger

"""
Clases de Ingredientes + Bebidas. Son Polimorphas, y  contienen el metodo de seleccion de
los ingredientes etc.
"""
#clase bebida

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

