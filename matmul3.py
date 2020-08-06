# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print ("Matriz de 4x4:")
import scipy as sp
from time import perf_counter


n = 4
A = sp.matrix(sp.rand(n,n))
B = sp.matrix(sp.rand(n,n))

t1 = perf_counter()

print(f"A = \n{A}")
print(f"B = \n{B}")

C = A*B     
t2 = perf_counter()
print(f"C = \n{C}")
print(f"C00 = \n{C[0,0]}")
print(f"A00 * B00 = \n{A[0,0]*B[0,0]}")


dt = t2 - t1

print(f"Tiempo transcurrido matriz 4x4: = {dt} s")




print ("Matriz de 100x100:")
m = 100
A2 = sp.matrix(sp.rand(m,m))
B2 = sp.matrix(sp.rand(m,m))
t3 = perf_counter()

print(f"A2 = \n{A2}")
print(f"B2 = \n{B2}")

C2 = A2*B2     
t4 = perf_counter()
print(f"C2 = \n{C}")
print(f"C200 = \n{C[0,0]}")
print(f"A200 * B200 = \n{A2[0,0]*B2[0,0]}")
dtt = t4 - t3

print(f"Tiempo transcurrido matriz 100x100: = {dtt} s")






print ("Matriz de 1000x1000:")
p = 1000
A3 = sp.matrix(sp.rand(p,p))
B3 = sp.matrix(sp.rand(p,p))
t5 = perf_counter()

print(f"A3 = \n{A3}")
print(f"B3 = \n{B3}")

C3 = A3*B3   
t6 = perf_counter()
print(f"C3 = \n{C}")
print(f"C300 = \n{C[0,0]}")
print(f"A300 * B300 = \n{A3[0,0]*B3[0,0]}")
ddtt = t6 - t5

print(f"Tiempo transcurrido matriz 1000x1000: = {ddtt} s")