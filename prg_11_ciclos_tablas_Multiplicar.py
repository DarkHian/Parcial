# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:03:01 2021

@author: Brahian
"""

#programar que leea una tabla y la imprima desde el 1 hasta el 20 y suma los 

#declarar variables


tabla=0
resultado=0
sumaResultados=0
multiplicador=1
contadordeciclo=1
conrepciclo=1

#leer el numero de la tabla la tabla para la cual vamos a realizar las operaciones

tabla= int(input("Tabla: "))

#leer multiplicador

multiplicador=int(input("multiplicador:"))



#inicio del ciclo



while(contadordeciclo <= multiplicador):
    
    
    
    resultado=tabla*multiplicador
    
    sumaresultado= sumaResultados + resultado
    
    contadordeciclo=contadordeciclo+tabla


    print(tabla,"*",multiplicador,"=",resultado)

print("la suma de los resultados es:",sumaResultados)








