# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:20:32 2020

@author: pauli
"""

from numpy import zeros, float32
from matplotlib.pylab import *
import numpy as np

def laplaciana_half(N, dtype=np.half):
    A=zeros ((N,N),dtype=dtype)
    
    for i in range (N):
        for j in range (N):
            
            if i+1==j:
                A[i,j]=-1
            if i-1==j:
                A[i,j]=-1
            if i==j:
                A[i,j]=2
                
    return A

def laplaciana_single(N, dtype=np.single):
    B=zeros ((N,N),dtype=dtype)
    
    for i in range (N):
        for j in range (N):
            
            if i+1==j:
                B[i,j]=-1
            if i-1==j:
                B[i,j]=-1
            if i==j:
                B[i,j]=2
                
    return B


def laplaciana_double(N, dtype=np.double):
    C=zeros ((N,N),dtype=dtype)
    
    for i in range (N):
        for j in range (N):
            
            if i+1==j:
                C[i,j]=-1
            if i-1==j:
                C[i,j]=-1
            if i==j:
                C[i,j]=2
                
    return C

