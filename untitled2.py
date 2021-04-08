# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:03:03 2021

@author: Brahian
"""

cuadradonum=0
cumuladorsum=0
contadorderepeticioneswhile=0




cantidadnumeros = int(input("cantidad de numeros: "))

while contadorderepeticioneswhile<cantidadnumeros:
    cuadradonum=contadorderepeticioneswhile*contadorderepeticioneswhile
    contadorderepeticioneswhile=contadorderepeticioneswhile+1
    acumuladorsuma=cumuladorsum+cuadradonum
    print("el cuadrado de :",contadorderepeticioneswhile,"es:",cuadradonum)
    print("la suma acumulada es:",acumuladorsuma)
    
#fin del ciclo
    
print("la suma de los cuadrados es:",acumuladorsuma)