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


