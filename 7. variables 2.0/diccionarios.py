#crando diccionarios con dict()
diccionario  = dict(nombre="Lucas",apellido="Dalto")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario1 = {frozenset(["dalto","rancio"]): "jajaj"}

#crando diccionarios con fromkeys()
diccionario2 = dict.fromkeys(["nombre","appelido"])

print(diccionario2)