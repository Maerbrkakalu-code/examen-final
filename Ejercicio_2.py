
from funciones import *

dirarchivo = "notas.txt"

creararchivo(dirarchivo)

tamanioLista = int(input("Ingrese la cantidad de números a generar en la lista: "))

listaoriginal = generarlista(tamanioLista, dirarchivo)

listanumraiz(listaoriginal, dirarchivo)
