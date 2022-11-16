from argparse import BooleanOptionalAction
from IPython.display import clear_output
import Hambclass
clear_output()
print('Bienvenido a Burger-Way! A continuacion cree su Hamburguesa.')
Hambclass.Pedido.pedido()
Hambclass.Pedido.balance()
Hambclass.Usuario.datos_user()
Hambclass.Usuario.metodos_pago()