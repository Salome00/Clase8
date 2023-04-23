def sumar_5_enteros():
    #Definición de variables
    lista = []
    ContadorWhile = 0
    tamano = 5
    suma = 0

    #se ingresan los números:
    while ContadorWhile < tamano:
        lista.append(int(input("Ingrese número " + str(ContadorWhile +1) + ": ")))
        ContadorWhile +=1

    #Sumando los números:
    ContadorWhile = 0
    while ContadorWhile - tamano:
        suma += lista[ContadorWhile]
        ContadorWhile +=1

    print("Los elementos de la lista son:")
    for numero in lista:
        print(numero,end=', ')

    print("\nLa suma de todos sus elementos es:")
    print(suma)