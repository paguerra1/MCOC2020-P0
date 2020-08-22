# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 10:40:28 2020

@author: pauli
"""



import numpy as np
from scipy import linalg
from time import perf_counter
from numpy.linalg import solve
from scipy.sparse import lil_matrix, csc_matrix
from scipy.sparse.linalg import spsolve, inv


# SE CREAN LAS DOS FUNCIONES PARA MATRIZ LAPLACIANA (LLENA Y DISPERSA)
def laplaciana_llena(N,t=np.double):
    A=np.identity(N,t)*2
    for i in range(N):
        for j in range (N):
            if i+1==j:
                A[i,j]=-1
            if i-1==j:
                A[i,j]=-1
    return A
                    

def laplaciana_dispersa(N,t=np.double):
    A=lil_matrix((N,N))
    for i in range(N):
        for j in range (N):
            if i==j:
                A[i,j]=2
            if i+1==j:
                A[i,j]=-1
            if i-1==j:
                A[i,j]=-1
    return csc_matrix(A)



# Tamaño creciente de matrices *2
# (Por simplicidad y por tiempo finalmente se realizó hasta 8192)
Nm= [2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384]

Numcorridas=4

# Se utiliza un codigo similar al de la entrega 6
# Los archivos ahora son cada uno de los casos
# {i} =0,1,2,3

for i in range(Numcorridas):
    nombres= [f"Complejidad_MATMUL_llena{i}.txt",f"Complejidad_MATMUL_dispersa{i}.txt",f"Complejidad_SOLVE_llena{i}.txt",f"Complejidad_SOLVE_dispersa{i}.txt",f"Complejidad_INV_llena{i}.txt",f"Complejidad_INV_dispersa{i}.txt"]
    archivos=[open(nombre,"w") for nombre in nombres]
   
    # Se crea el ensamblaje y solucion donde se operara luego
    for N in Nm:
        ensamblaje = np.zeros((len(archivos)))
        solucion = np.zeros ((len(archivos)))
        
        print (f"N={N}")
        
      
# ------------------------------------------------------------------  
  #CASO1: MATMUL- Matriz llena:
# ------------------------------------------------------------------  
        # tiempo 1
        t1=perf_counter()
        
        # Se crean ambas matrices:
        A= laplaciana_llena(N)
        B= laplaciana_llena(N)
        
        # tiempo 2:
        t2=perf_counter()
        
        #Matmul
        C= A@B
                
        #tiempo 3
        t3=perf_counter()
        
        #diferencia de tiempo
        dt1 = t2 - t1
        dt2 = t3 - t2
        
        #Se agregan los datos obtenidos de las dos diferencias de tiempo 
        ensamblaje[0]= dt1
        solucion[0]= dt2
        
        
# ------------------------------------------------------------------        
   #CASO2: MATMUL- Matriz dispersa:       
# ------------------------------------------------------------------          
        t1=perf_counter()
        
        A= laplaciana_dispersa(N)
        B= laplaciana_dispersa(N)
        t2=perf_counter()
            
        C= A@B
        t3=perf_counter()

        dt1 = t2 - t1
        dt2 = t3 - t2
        
        ensamblaje[1]= dt1
        solucion[1]= dt2
        
# ------------------------------------------------------------------         
   #CASO3: SOLVE- Matriz llena:
# ------------------------------------------------------------------  
        t1=perf_counter()

        A= laplaciana_llena(N)
        b = np.ones(N,dtype=np.double)
        t2=perf_counter()
            
        C =solve(A,b)
        t3=perf_counter()

        dt1 = t2 - t1
        dt2 = t3- t2
        
        ensamblaje[2]= dt1
        solucion[2]= dt2
        
        
# ------------------------------------------------------------------          
   #CASO4: SOLVE-Matriz dispersa:       
# ------------------------------------------------------------------  
        t1=perf_counter()

        A= laplaciana_dispersa(N)
        b = np.ones(N,dtype=np.double)
        t2=perf_counter()
            
        C=spsolve(A,b)
        # c=np.linalg.solve
        t3=perf_counter()

        dt1= t2 - t1
        dt2= t3 - t2
        
        ensamblaje[3]= dt1
        solucion[3]= dt2
        
# ------------------------------------------------------------------          
   #CASO5: INV- Matriz llena:
# ------------------------------------------------------------------        
        t1=perf_counter()
        
        A= laplaciana_llena(N)
        t2=perf_counter()
        
        A_inv= linalg.inv(A)
        t3=perf_counter()

        dt1= t2 - t1
        dt2= t3 - t2
        
        ensamblaje[4]= dt1
        solucion[4]= dt2
             
# ------------------------------------------------------------------          
   #CASO6: INV- Matriz dispersa:       
# ------------------------------------------------------------------         
        t1=perf_counter()
        A= laplaciana_dispersa(N)
        t2=perf_counter()
        
        A_inv= inv(A)
        t3=perf_counter()

        dt1= t2 - t1
        dt2= t3 - t2
               
        ensamblaje[5]= dt1
        solucion[5]= dt2
        
          
    
    # Se agregan los resultados al archivo de texto:
        for j in range(len(archivos)):
            archivos[j].write(f"{N} {ensamblaje[j]}{solucion[j]}\n")
            archivos[j].flush()
        
[archivo.close()for archivo in archivos]


