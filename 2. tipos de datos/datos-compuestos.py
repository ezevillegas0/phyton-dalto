#datos que tienen datos simples u otro tipo de datos que se pueden agrupar.

#LISTA - sirve para agrupar datos. 
lista = ["lucas dalto", "soy dalto", True, 1.85]
lista[3] = "maquinola" #se puede modificar

#TUPLA - no se puede modificar. se puede redefinir.
tupla = ("lucas dalto", "soy dalto", True, 1.85)

#CONJUTNO (SET) - no tienen un orden fijo, los elementos pueden cambiar. no se puede modificar el contenido de los elementos. se puede redefinir.
conjunto = {"lucas dalto", "soy dalto", True, 1.85, "soy dalto"} #en un conjunto no puede haber datos duplicados. 
#print(conjunto[1]) -> no se pueden mostrar los elementos a partir del indice.
print(conjunto)

#DICCIONARIO (DICT) - key : value
diccionario = {
    'nombre' : "lucas dalto",
    'canal' : "soy dalto",
    'esta_emocionado' : True,
    'altura' : 1.85,
    'dato_duplicado' : "soy dalto"
}
print(diccionario['nombre'])