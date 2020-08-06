# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 23:29:07 2020

@author: pauli
"""
print ("Ejercicio Hola.py")
nombre = "Paulina"
dia = 5

print("Forma 1:")
print("hola Paulina es el 5 de Agosto")

print("Forma 2:")
print("hola " + nombre + " es el " + str(dia) + " de Agosto")

print("Forma 3:")
print("hola {nombre} es el {dia} de Agosto".format(dia=dia, nombre=nombre))

print("Forma 4:")
print(f"hola {nombre} es el {dia} de Agosto")

print("Ejemplo 2 - Forma 1:")
print("hola hola hola hola hola hola hola")

print("Ejemplo 2 - Forma 1:")
print("hola "*100)