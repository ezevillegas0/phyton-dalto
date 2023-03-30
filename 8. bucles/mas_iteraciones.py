frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]

#evitando que se coma una fruta con la sentencia continue.
for fruta in frutas:
    if fruta == 'granada':
        continue
    if fruta == 'banana':
        continue
    print(f"me voy a comer una {fruta}")
print("bucle terminado")
    
print("---------------------") 

#evitar que el bucle se siga ejecutando con un break.
for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta == 'pera':
        break
print("bucle terminado")

#recorrer una cadena de texto
cadena = "hola dalto"

for letra in cadena:
    print(letra)
    
#duplicamos los numeros con un for en una sola linea de codigo.
numeros = [2,5,8,10]

numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)