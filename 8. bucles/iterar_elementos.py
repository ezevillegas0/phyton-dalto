lista_animales = ["gato","perro","loro","cocodrilo"]
lista_numeros = [10,62,12,72]

#recorriendo la lista animales
for animal in lista_animales:
    print(f"ahora la varible animales es igual a: {animal}")
    
#recorriendo la lista de numero y multiplicamos por 10
for numero in lista_numeros:
    resultado = numero * 10
    print(resultado)
    
#recorriendo dos listas a la vez con zip(). para que esto funcione ambas listas deben tener la misma cantidad de elementos
for numero,animal in zip(lista_animales,lista_numeros):
    print(f"recorriendo la lista 1 : {numero}")
    print(f"recorriendo la lista 2 : {animal}")
    
#devolviendo numeros del 10 al 19 con range()
for num in range(10,20):
    print(num)
    
#recorriendo una lista con su indice con enumerate()
for num in enumerate(lista_numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
#recorriendo usando un else
for numero in lista_numeros:
    print(f"ejecutamos el ultimo bucle, valor actual{numero}")
else:
    print("el bucle termino")
    
#todo lo anterior funciona exactamente igual para tuplas