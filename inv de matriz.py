# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 19:39:43 2021

@author: Brahian
"""
import numpy as np
A=np.array([[2,1],[4,3]])

x1=np.array([2,2])

x=x1.T

b=A.dot(x)

A_inv= np.linalg.inv(A)

sol=A_inv.dot(b)



print()
print(b)
print()
print("inversa:")
print(A_inv)
print()
print("solucion con inv")
print(sol)

