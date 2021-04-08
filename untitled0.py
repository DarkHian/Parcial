# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:26:37 2021

@author: Brahian
"""
import random


cantnumeros=0
contadorrepdewhile=0
numero=0
acumuladorsuma=0
promedionumerosaleat=0.0

#entradas

#varialbles segunda parte del ejercicio
acumuladorpositivos=0
acumuladornegativos=0
promediopositivos=0.0
promedionegativos=0.0

contadoredepositivos=0
contadordenegativos=0.0

cantnumeros=int(input("cantidad de numeros:"))

#procesos
#ciclos While
while contadorrepdewhile<cantnumeros:
        numero=random.randint(0,1000)
        acumuladorsuma=acumuladorsuma+numero
        contadorrepdewhile=contadorrepdewhile+1
        #segunda parte del ejercicio
        if numero>0:  #calculo para numeros positivos
            print("numero positivo:",numero)
            acumuladorpositivos=acumuladorpositivos+numero
            contadoredepositivos=contadoredepositivos+1
        else:#calculos para numeros negativos
            print("numero negativo:",numero)
            acumuladornegativos=acumuladornegativos+numero
            contadordenegativos=contadordenegativos+1
        
#fin del ciclo
promedionumerosaleat= acumuladorsuma/contadorrepdewhile

promediopositivos=acumuladorpositivos/contadoredepositivos
promedionegativos=acumuladornegativos/contadordenegativos

#salida
print("suma de numeros aleatorios:",acumuladorsuma)
print("promedio de numeros aleatorios:",promedionumerosaleat)

#salida de numeros negativos y positivos

print("suma de numeros positivos",acumuladorpositivos)
print("suma de numeros negativos",acumuladornegativos)
print("promedio de numeros positivos",promediopositivos)
print("promedio de numeros negativos",promedionegativos)
