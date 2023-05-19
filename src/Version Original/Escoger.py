from IPython.display import clear_output
 
##Metodo de escoger el menu de ingredientes.
   
def escoger(menu):
    clear_output()
    print('Estas son nuestras opciones:\n')
    print(*menu, sep=", ")
    selec=input('\nCual desea?\n')
    return selec
