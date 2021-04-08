# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:58:32 2021

@author: Brahian
"""

def mostrar_mayor(v1,v2,v3,v4):
        
    print("El valor mayor de los tres numeros es")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3 and v2>v4:
            print(v2)
        else:
            if v3>v4:
                print(v3)
            else:
                print(v4)

def cargar():
    v1=int(input("Primer numero:"))
    v2=int(input("segundo numero:"))
    v3=int(input("Tercer numero:"))
    v4=int(input("cuarto valor:"))
    mostrar_mayor(v1,v2,v3,v4)


cargar()












