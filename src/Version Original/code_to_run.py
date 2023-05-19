from argparse import BooleanOptionalAction

from IPython.display import clear_output

import Hambclass
import Usuario
import Escoger

clear_output()
print('\nBienvenido a Burger-Way! A continuacion cree su Hamburguesa.\n')
tam = int(input('Cuantas Hamburguesas quiere pedir?\n'))
Hambclass.Pedido.total_balance=0
for x in range(0,tam):
    print(f'Hamburguesa #{x + 1}: \n')
    Hambclass.Pedido.pedido()
    Hambclass.Pedido.balance()

Usuario.User.datos_user()
Usuario.User.metodos_pago()
