# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 22:30:55 2021

@author: Brahian
"""
matriz = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
i = 1 #columna que queremos obtener
indice_fila = 0
columna = []
while indice_fila<len(matriz):
	columna.append(matriz[indice_fila][i])
	indice_fila += 1
    
print(matriz[i])

