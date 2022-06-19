

def creararchivo(path):

        file = open(path, "a+")
        file.close()


def generarlista(numero, path):

        import random

        milista = []

        for indice in range(1, numero + 1):
                milista.append(random.randint(1, 20))

        file = open(path, "a+")
        file.writelines(str(milista))
        file.close()

        return milista



def listanumraiz(lista, path):

        from math import sqrt as raiz

        listanueva = []

        for numero in lista:

                listanueva.append(raiz(numero))

        file = open(path, "a+")
        file.writelines("\n"+str(listanueva))
        file.close()


