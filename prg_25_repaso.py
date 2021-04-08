# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:33:55 2021

@author: Brahian
"""

#programa que lee numero enteros y calcula el promedio


#Declarar las variables

#variable que almacena los numeros que digite el usuario
num= 0
#variable que almacena la suma de los numeros positivos
sum_=0
#variable que almacena la media
media= 0.0
#variable  que almacena la cantidad de numerosdigitados
cantidad_elementos= 0

#Lectura del primer numero
num= int(input("numero:"))

while (num>0):
    sum_=sum_+num
    #lectura de los otros numeros
    num=int(input("numero:"))
    cantidad_elementos=cantidad_elementos+1

if cantidad_elementos !=0:
    #calcular la media
    media=sum_/cantidad_elementos

else:
    print("no hay numero para calcular la media")








#termina el ciclo
#calcular la media
media= sum_/cantidad_elementos
print()
print("la media es:",media)







