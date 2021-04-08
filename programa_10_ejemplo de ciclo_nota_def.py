# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:36:35 2021

@author: Brahian
"""

#cantidad de estudiantes

cantEst=int(input("Cantidad de estudiantes:"))
#variable para controlar el ciclo
conrep=0
#variable para calcular la nota del grupo
sumdefgrup=0.0
promdefgrup=0.0

#entrada

while(conrep < cantEst):
     #instrucciones a repetir
     
     #pedir nombre
     numeroEst=input("Nombre del estudiante=")
     
     #perdir 3 notas 

     not_1est=float(input("parcial 1:"))
     not_2est=float(input("parcial 2:"))
     not_3est=float(input("parcial 3:"))

     #sacar el promdio

     notadef= (not_1est+not_2est+not_3est)/3

     #acumulo defnitiva del grupo
     sumdefgrup=sumdefgrup+notadef
     #Incrementar la variable que controla el ciclo
     conRep = conrep+1

     # Calcular el promedio del grupo
     notProDefGru = sumdefgrup/cantEst




     #mostrar

     print()
     print(f"nota definitiva es:{notadef:.2f}")
     print()
     print()
     
     
     
     #incremento del repetidor
     conrep=conrep+1
     
#acumulo defnitiva del grupo
sumdefgrup=sumdefgrup+promdefgrup

#  Imprimir la nota promedio del grupo
print(f"2. La nota promedio del grupo es :{notProDefGru:.2f}")