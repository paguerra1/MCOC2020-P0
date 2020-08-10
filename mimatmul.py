# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:07:46 2020

@author: pauli
"""


import numpy as np
from scipy import rand

def mimatmul(A,B):
    # Se genera una lista vacía, para agregar el resultado luego
    C=[]

    # Se itera a traves de las filas de A
    for n in range(len(A)):
        fila=[]
       # Se itera a través de las columnas de B
        for m in range(len(A)):
            fila.append(0)
        # se agregan ceros a lista C 
        C.append(fila)
        
        
    #A la listas de ceros, se le suman las filas y columnas correspondientes 
    for i in range(len(A)):
        for j in range(len(B[0])):
           for k in range(len(B)):
               C[i][j] += A[i][k] * B[k][j]
   
    return C