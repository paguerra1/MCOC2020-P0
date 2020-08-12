# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:54:13 2020

@author: pauli
"""


from time import perf_counter
from numpy.linalg import inv
from laplaciana import laplaciana_single

Nm= [2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,600,800,1000,2000,5000]

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
        A= laplaciana_single(N)
        B= laplaciana_single(N)
        
        # tiempo 1
        t1=perf_counter()
        
        ainv=inv(A)
        binv=inv(B)
        
        
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
