#definiendo una variable
a = 2
b = 10
c = a + b
nombre = "lucas"
nombreCompleto = " Lucas Dalto" #camelCase
nombre_completo = "Lucas Dalto" #snake_case

numero = 10
numero += 4 #toma el valor anterior y suma lo que indiquemos
numero += 6

#concatenar con +
bienvenida  = "Hola " + nombre + " como estas?"
#concatenar con f-strings
bienvenida1  = f"Hola {nombre} como estas?"

del bienvenida #elimina bienvenida
print(bienvenida1)

# operadores de pertenencia ( in - not in)
print("ola" in bienvenida1) #true
print("pedro" in bienvenida1) #false

print("pedro" not in bienvenida1) #true
print("Hola" not in bienvenida1) #false

#en las variables definimos datos, estos datos pueden ser simples o compuestos.