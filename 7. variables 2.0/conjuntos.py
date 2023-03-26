#los datos de set no son modificables.

#crando un conjunto con set()
conjunto = set(["dato1","dato2"])
conjunto_con_tupla = set(["dato1",("datoenlista1","datoenlista2")])
#metiendo un conjunto dentro de otro conjunto.
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}
print(conjunto2)

#teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}
#vemos si es un subconjunto de otro conjunto
resultado = conjunto2.issubset(conjunto1)
resultado1 = conjunto2 <= conjunto1
#vemos si es un superconjunto de otro conjunto
resultado3 = conjunto2.issuperset(conjunto1)
resultado4 = conjunto2 >= conjunto1
#vemos si hay algun numero en comun
resultado5 = conjunto2.isdisjoint(conjunto1) #devuelve True cuando los conjuntos que se comparan no tienen ningun numero igual.
print(resultado5)