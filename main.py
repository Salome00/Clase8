import problema1
from alumnos import alumnos


'''
hasta ahora se ha trabajado con
variables que permiten almacenar
un único valor
'''

edad = 12

altura = 1.50

nombre = "santiago"

estado = True

'''
En python se puede usar una 
variable que almacena una colección 
de datos y luego accederla
usando un sibíndice
'''

#lista de enteros
lista1 = [10, 5, 3 , 9]

#lista de decimales
lista2 = [1.78, 2.66, 1.55, 27.4, 11.9]

#lista de string
lista3 = ["lunes", "Martes", "Miercoles"]

'''
Lista de elementos de distintos tipos
'''

lista4 = ["Santiago", 20, 1.70, False]




if __name__ == '__main__':

    '''
    Cantidad de elementos de cada lista:
    '''

    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))

    print()
    print(lista1)
    lista1[0] = 1
    print()
    print(lista1)

    print(lista1[3])

    print()

    problema1.sumar_5_enteros()

    print()

    alumnos()




