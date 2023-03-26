#metodos de listas.


# LIST - crea una lista. es una funcion.
lista = list(["hola","dalto",34, True])

#----------------------------------#

# LEN - devuelve la cantidad de elementos de una lista. es una funcion.
cadena = "alfaveta"
resultado = len(lista)

#----------------------------------#

# APPEND - agrega un elemento a la lista.
lista.append("jajaj")
# INSERT - agrega un elemento a la lista en el indice especificado.
lista.insert(2, "toma mama")
# EXTEND - agrega varios elementos a la lista.
lista.extend([False, 2023])

#----------------------------------#

# POP - elimina un elemento de una lista, pide el indice y devuelve el valor.
lista.pop(0)# -1 se elimina el ultimo elemento de la lista, -2 el anteultimo.
# REMOVE - remueve un elemento de una lista, pide un valor.
lista.remove("toma mama")
# CLEAR - elimina todos los elementos de una lista.
lista2 = list(["hola",12])
lista2.clear()

#----------------------------------#

# SORT - ordena una lista de forma ascendente a descendente. no funciona si tiene strings.
lista2.sort()
# REVERSE - invierte los elementos de una lista.
lista.reverse()

print(lista)