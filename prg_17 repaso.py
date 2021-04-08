# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:00:43 2021

@author: Brahian
"""
"""
programa que lee el nombre y la nota definitiva
de 3 materias(basic,fortran y pascal) de N estudiantes.
condicion de salida nombre=***
"""


#Area de declaracion de variable
#primer variable
var_en_nombre= "***"
var_en_basic=0.0
var_en_fortran=0.0
var_en_pascal=0.0

var_conest= 0
var_p_s_med_estu= 0.0

# Leer  nombre
var_en_nombre= input("digite el nombre del estudiante:")

#Ciclo While
#! es negacion
while (var_en_nombre!="***"):
    # int es convertir a numero entero y float es a numero real osea con decimales
    #float permite leer y sacar numero decimales 0.0
    var_en_basic= float(input("Definitiva Basic:"))
    var_en_fortran= float(input("Definitiva fortran:"))
    var_en_pascal= float(input("Definitiva pascal:"))

#proceso para calcular la media del estudiante
    var_p_s_med_estu=(var_en_basic+var_en_fortran+var_en_pascal)/3
    print("su media es:",var_p_s_med_estu)
    #input es para leer lo que se escribe en la cosnola
    var_en_nombre= input("digite nobre del estudiante:")
    var_conest=var_conest+1
    

#fin del ciclo
print("cantidad de estudiantes:",var_conest)
































