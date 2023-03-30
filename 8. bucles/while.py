#creando un contador auto incrementable.
contador = 0
#mientras que la condicion se cumpla, el bucle se va a ejecutar.
while contador < 10:
    print(contador) #si no le sumo numeros al contador se ejecuta de manera infinita.
    contador+= 1
print("el while llego a su fin")