import random


def lista1_aleatorio():

    listanumero = []

    for indice in range(1, 11):
        listanumero.append(random.randint(1, 20))

    return listanumero


lista1_original = lista1_aleatorio()


print("Mi lista 1 es: {}".format(lista1_original))


def lista2_noduplicados(milista):

    listaresultante = []

    for element in milista:

        if element not in listaresultante:

            listaresultante.append(element)

    return listaresultante


lista2_nodup = lista2_noduplicados(lista1_original)

print("Mi lista 2 con número no repetidos es: {}".format(lista2_noduplicados(lista1_original)))


def lista3_mayor_menor(mislista):

    mislista.sort(reverse=True)

    return mislista


print("Mi lista 2 ordenador de mayor a menor es: {}".format(lista3_mayor_menor(lista2_nodup)))


def lista4_menor_mayor(mislista):

    mislista.sort()

    return mislista


print("Mi lista 2 ordenador de menor a mayor es: {}".format(lista4_menor_mayor(lista2_nodup)))


def lista5_mayor_numero(mislista):

    mayor = 0
    for numero in mislista:

        if numero > mayor:

            mayor = numero

    return mayor


print("El mayor número de mi lista 2 es: {}".format(lista5_mayor_numero(lista2_nodup)))

