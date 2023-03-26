#metodos de diccionarios.

diccionario = {
    "nombre" : "Lucas",
    "apellido" : "Dalto",
    "subs" : 1000000
}

diccionario1 = {
    "nombre" : "Lucas",
    "apellido" : "Dalto",
    "subs" : 1000000,
    "edad" : 18
}

# keys() -> devuelve las claves. tambien nos sirve para iterar.
claves = diccionario.keys()
# get () ->devuevlve el valor de una clave.
valor_claves = diccionario.get("nombre")
# clear() -> elimina todos los elementos.
eliminar_todos_elementos = diccionario1.clear()
# pop() -> elimina un elemento.
eliminar_un_elemento = diccionario.pop("nombre")
# items() -> para iterar dict.
diccionario_iterable = diccionario.items()

print(diccionario_iterable)