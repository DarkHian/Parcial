# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:25:57 2021

@author: Brahian
"""

print("ejemplo del profe")
import numpy as np
Matriz = np.arange (9)
np.random.shuffle (Matriz)
Matriz = Matriz.reshape((3,3))
print(Matriz)

print("yo modificando y haciendo otra fila")
Matriz2 = np.arange (8)
np.random.shuffle (Matriz2)
Matriz2 = Matriz2.reshape((1,8))
print(Matriz2)

print("yo modificando y haciendo otra pero en columna")
Matriz3 = np.arange (8)
np.random.shuffle (Matriz2)
Matriz3 = Matriz3.reshape((8,1))
print(Matriz3)


np.linalg.inv=(Matriz3)

