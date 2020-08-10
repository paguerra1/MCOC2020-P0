# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 10:50:18 2020

@author: pauli
"""

import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

plt.figure()

# Se crea una funcion para llamarla desde timing_matmul:

def graficar(Numcorridas):
    b=sp.loadtxt("matmul0.txt")
    x_=[]
    Nm= b[:,0]
  
        
    y_t=[]
    tiempo=b[:,1]
 

    y_m=[]
    memoria=b[:,2]
  
        
       
    for i in range (1,Numcorridas):
        b=sp.loadtxt(f"matmul{i}.txt")
        
        tiempo=sp.vstack((tiempo,b[:,1]))
       
    
        
    
    
    # Eje y de tiempo transcurrido:
    yticks=[0.0001,0.001,0.01,0.1,1,10,60,600]
    yticks_text=["0.1 ms","1ms","10ms","0.1 s","1 s","10 s", "1 min", "10 min"]
    # Eje y de memoria usada:
    yticks2=[1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000]
    yticks_text2=["1 KB","10KB","100KB","1MB","10MB","100MB","1GB","10GB"]
    # Eje x:
    xticks=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
    xticks_text=["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
    
    
    
    
    plt.subplot(2,1,1)
    plt.loglog(Nm,tiempo.T,"-o")
    plt.title("Rendimiento A@B")
    plt.grid(True)
    plt.xlabel("Tamaño de la matriz N")
    plt.ylabel("Tiempo transcurrido")  
    
    plt.yticks(yticks, yticks_text)
    plt.xticks(xticks,xticks_text, rotation=45)
    plt.tight_layout()
   
    
   
    plt.subplot(2,1,2)
    plt.loglog(Nm,memoria,"-o")
    plt.xlabel ("Tamaño de la matriz N")
    plt.ylabel ("Uso de la memoria")
    plt.grid(True)
    plt.yticks(yticks2, yticks_text2)
    plt.xticks(xticks,xticks_text, rotation=45)
    plt.axhline(10000000000,linestyle='--',color='k')
    plt.show()       
    
    


