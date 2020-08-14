# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 12:30:51 2020

@author: pauli
"""

from time import perf_counter
import numpy as np

# se crea la funcion de Laplacian Matrix
from numpy import float32
def laplaciana(N, d= float32):
    A=-(np.eye(N,k=-1,dtype=d))+2*(np.eye(N,dtype=d))+-(np.eye(N, k=+1,dtype=d))
    return A

# Tamaño de matrices

Nm= [2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,600,1000,2000,5000,10000]

Numcorridas=10

nombres=["A_invB_inv.txt","A_invB_npSolve.txt"]
archivos=[open(nombre,"w") for nombre in nombres]

for N in Nm:
    dts=np.zeros((Numcorridas,len(archivos)))
    print (f"N={N}")
       
    #Forma 1 
    for i in range (Numcorridas):
        # Se crea matriz laplaciana A:
        A=laplaciana(N)
        
        # Se crea un vector de unos:
        B=np.ones(N)
        # tiempo 1
        t1=perf_counter()
        
        # Se invierte la matriz A
        A_inv=np.linalg.inv(A)
        
        # Se multiplica por vector B
        A_invB=A_inv@B
        # tiempo 2
        t2=perf_counter()
        
        # diferencia de tiempo
        dt=t2-t1
        
        # agregar al archivo en primera columna
        dts[i][0]=dt
        
        
        
        
        # Forma 2: lo mismo pero usando np.linalg.solve(A,B)
        # Se crea matriz laplaciana A:
        A=laplaciana(N)
        
        # Se crea un vector de unos:
        B=np.ones(N)
        # tiempo 1
        t1=perf_counter()

        A_invB=np.linalg.solve(A,B)
        # tiempo 2
        t2=perf_counter()
        
        # diferencia de tiempo
        dt=t2-t1
        # agregar al archivo en segunda columna
        dts[i][1]=dt
        
    print ("dts: ", dts)
    
    # Se calcula el promedio de los tiempos:
    dts_mean=[]
    for j in range(len(archivos)):
        dts_mean.append(np.mean(dts[:,j]))
        
    print("dts_mean: ", dts_mean)
        
    
    # Se agregan los resultados al archivo de texto:
    for j in range(len(archivos)):
        archivos[j].write(f"{N} {dts_mean[j]}\n")
        archivos[j].flush()
        
[archivo.close()for archivo in archivos]



# Se crea la función para graficar lo anterior

import matplotlib.pyplot as plt
import numpy as np

plt.figure()

def graficar(Nombres):
 
    # Eje y de tiempo transcurrido:
    yticks=[0.0001,0.001,0.01,0.1,1,10,60,600]
    yticks_text=["0.1 ms","1ms","10ms","0.1 s","1 s","10 s", "1 min", "10 min"]
  
    # Eje x:
    xticks=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
    xticks_text=["10","20","50","100","200","500","1000","2000","5000","10000","20000"]

    plt.figure()
    
    for nombre in nombres:
        data=np.loadtxt(nombre)
        Nm=data[:,0]
        dts=data[:,1]
        
        print("Ns: ", Nm)
        print ("dts: ", dts)
        
        plt.loglog(Nm,dts.T,"-o", label=nombre)
        plt.ylabel("Tiempo transcurrido (s)")
        plt.xlabel("Tamaño de matriz")
        plt.grid(True)
        plt.title("Desempeño Ax=b")
        
        plt.xticks(xticks,xticks_text, rotation=45)
        plt.yticks(yticks, yticks_text)
        
    plt.tight_layout()
    plt.legend()  
    plt.show()
      
    
nombres=["A_invB_inv.txt","A_invB_npSolve.txt"]


graficar(nombres)        
        


