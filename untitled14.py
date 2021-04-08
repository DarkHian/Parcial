



#Declaración de variables
trabajador: nombre

if ( horas <= 35 ) entonces
    salarioBruto=  horas * tarifa
else
salarioBruto ( 35 * tarifa ) + ( horas -35) * 1.5 * tarifa
fin_si
si salarioBruto <= 20000 entonces
impuestos ← 0
si_no
si ( salarioBruto > 20000 ) y ( salarioBruto <= 35000 ) entonces
impuestos ← ( salarioBruto – 20000 ) * 0.20
si_no
impuestos
fin_si
fin_si
salarioNeto ← salarioBruto – impuestos
