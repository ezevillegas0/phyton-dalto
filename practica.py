#imprimir nombre con input
nombre = input("ingresa tu nombre: ")

#concatenar con +
bienvenida = "hola " + nombre + " como estas?"
#concatenar con f-strings
bienvenida1 = f"Hola {nombre} como estas?"

print(bienvenida1)

40 #entero(int)
405#flotante(float)


#ejercicio con if
edad = int(input("ingresa tu edad: "))

if edad >= 18 :
    print("es mayor de edad, puede pasar")
else:
    print("es menor de edad, no puede pasar")
    

#calculadora
numero = int(input("ingresa un numero para operar: "))
resultado = (numero) * 2 #devuelve un string.
resultado2 = int(numero) * 2 #devuelve un numero.
resultado3 = float(numero) * 2 #devuelve un numero con coma.
print(resultado)


lista_animales = ["gato","perro","loro","cocodrilo"]
lista_numeros = [10,62,12,72]

#recorriendo la lista animales
for animal in lista_animales:
    print(f"ahora la varible animales es igual a: {animal}")
    
    
    
#control H para buscar y reemplazar