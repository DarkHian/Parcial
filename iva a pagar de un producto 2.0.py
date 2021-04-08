# Factura a pagar


def f_titulo():
    print("calculo valor con iva")
    
def f_despedida():
    print(",,,,Adios,,,")
    
#inicio
def f_valorfactura(): #encabezado de la funcion
    #definicion de variables
    va_ente=""
    va_cantiartic=0
    va_valorart=0.0
    val_neto=0.0
    val_ivapag=0.0
    val_totalpag=0.0
        
    #constante
    porcentagiva=0.19
    
    vps_netpag=0.0
    vps_ivapag=0.0
    vps_totpag=0.0
    
    #entrada de datos
    va_ent= input("articulos:")
    va_cantiartic= int(input("cantidad:"))
    va_valorart=float(input("valor unitario:"))
    
    
    #procesos
    vps_netpag=va_cantiartic*va_valorart
    vps_ivapag=val_neto*porcentagiva
    vps_totpag=vps_netpag+vps_ivapag
    
    
    
    
    
    
    

    #salidas
    print("neto:")
    
    
    
    
    
    
    
print ()
print ("valor neto:")
print (vps_netpag)
print ()
print ("valor iva:")
print (vps_ivapag)
print ()
print ("valor total:")
print (vps_totpag)


#llamado a la funcion titulo

f_titulo()
f_valorfactura()

f_despedida()




