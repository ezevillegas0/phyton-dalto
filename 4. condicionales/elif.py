ingreso_mensual = 72000
gasto_mensual = 80000

#operadores anidados y elif ( else if )

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas bien economicamente")
    else:
        print("estas gastando mucho")

elif ingreso_mensual > 1000: #else if = elif
    print("estas bien economicamente en latinoamerica")
    
else:
    print("sos pobre")