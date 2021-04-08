# -*- coding: utf-8 -*-


hs=input("Ingrese las horas trabajadas: ")
phs=input("Ingrese su sueldo por hora: ")
extras=hs-40
extrasb=hs-48
if hs<40 and hs>0:
    sueldo=hs*phs
    print ("su sueldo es:",sueldo)
    print("no posee horas extras")
if hs>=40 and hs<=48:
    sueldo1=(extras*phs)*2
    sueldo=hs*phs
    sueldot=sueldo+sueldo1
    print ("su sueldo es:",sueldo)
    print( "el sueldo de sus horas extras es:",sueldo1)
    print( "su sueldo total es",sueldot)
elif hs>48:
    sueldo1=(extras*phs)*2
    sueldo2=(extrasb*phs)*3
    sueldo=hs*phs
    sueldot=sueldo+sueldo1+sueldo2
    print ("su sueldo es:",sueldo)
    print("su sueldo de sus primeras 8 horas extras es:",sueldo1)
    print("su sueldo de las demas horas extras es:",sueldo2)
    print("su sueldo total es",sueldot)
else:
    print( "el numero que ingrese es incorrecto intente de nuevo POR FAVOR !")
