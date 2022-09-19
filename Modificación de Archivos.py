# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:13:10 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

nombre = input("Ingres el nombre del archivo con su extensión: ")
archivo_escritura = open(nombre, "w", encoding="UTF-8")
n_car = int(input("Ingrese el número límite de carácteres de cada linea: "))

linea = ""
contador = 0
while linea != "no más":
    contador += 1
    linea = input("Ingrese un mensaje " + str(contador) + " al archivo: ")
    if linea == "no más":
        break
    inicio = 0
    while inicio < len(linea):
        archivo_escritura.write(linea[inicio:(inicio + n_car)] + "\n")
        inicio += n_car

archivo_escritura.close()
