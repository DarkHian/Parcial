# -*- coding: utf-8 -*-

"""Punto 3: Se desea obtener la nómina semanal —salario neto— de los N (Leídos por teclado) empleados 
  de una empresa, cuyo trabajo se paga por horas y del modo siguiente:

• las horas inferiores o iguales a 35 horas (normales) se pagan a una tarifa determinada que se debe
 introducir por teclado al igual que el número de horas trabajadas, el nombre del trabajador, género 
 y 1,2 o 3 de acuerdo a la sección donde trabaje
• las horas superiores a 35 se pagarán como extras a un promedio de 1,5 horas normales,
• los impuestos a deducir a los trabajadores varían en función de su sueldo mensual:
  Salud 12,5% del salario
  ICBF 4% del salario
  Retención en la fuente según la tabla anexa:
       de 2’000.000 a 3´000.000 5%
       de 3’000.001 a 4’000.000 7%
       de 4’000.001 a 5’000.000 9%
       de 5’000.000 en adelante 11%
Imprima el desprendible de pago detallado para cada empleado
Imprima la planilla de totales de pago de la empresa (Total Empleados, Total Horas, Total extras, pago horas, pago extras, etc)
Imprimir la planilla de totales los acumulados por sección.
Imprimir la planilla de totales los acumulados por género."""

#digitar datos
    
Nombre=input("Nombre:")

Genero=input("Genero:")

Seccion_trabajo=input("Seccion de trabajo:")

Horas_trabajadas=int(input("Horas:"))

Sueldo_por_hora=float(input("sueldo Hora:"))

horas_ex=int(input("horas extras:"))







#ejercicios
salario_ordinario= Horas_trabajadas * Sueldo_por_hora
   
horas_extras_b=(horas_ex)*1.5

horas_extras=Sueldo_por_hora*horas_extras_b

Valor_acum=horas_extras+salario_ordinario

Salud_des=0.125

ICBF=0.04



print()
print("------FACTURA-------")

print("NOMBRE DEL TRABAJADOR",Nombre)
print()
print("GENERO:",Genero)
print()
print("SECCION:",Seccion_trabajo)
print()
print("Salario neto")
print()
print(salario_ordinario)
print()
print("pago por horas Extra")
print()
print(horas_extras)
print()
print("total")
print()
print(Valor_acum)
print()
print()
print()
