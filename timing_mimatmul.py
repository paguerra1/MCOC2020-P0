# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 21:07:59 2020

@author: pauli
"""
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
from scipy import rand, savetxt
from time import perf_counter


Nm= [2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,600,800,1000,2000,5000,10000]

Numcorridas=10

for i in range (Numcorridas):
    # Se crean las listas
    tiempo=[]
    memoria=[]
    
    nombre=(f"matmul{i}.txt")
    # Se crea archivo
    archivo=open(nombre,"w")
    
    for N in Nm:
        print (f"N={N}")
        # Las dos matrices
        A= rand(N,N)
        B= rand(N,N)
        
        # tiempo 1
        t1=perf_counter()
        
        from mimatmul import mimatmul
        C=mimatmul(A,B)
        
        # tiempo 2
        t2=perf_counter()
        
        # diferencia de tiempo
        dt=t2-t1
        
        # cantidad de memoria utilizada
        size=3*(N**2)*8
        
        # Se agrega el tiempo y memoria a sus respectivas listas
        tiempo.append(dt)
        memoria.append(size)
        
        
        # escribir dentro del archivo creado
        archivo.write(f"{N} {dt} {size}\n")
    
        
        print(f"El tiempo trasncurrido fue : {dt} s")
        print (f"La memoria usada: {size} bytes")
        
        
        archivo.flush()
        
    archivo.close()
    


        
from graficar2 import graficar

graficar(Numcorridas)


        
        
        
        
        
        
        
        
        
