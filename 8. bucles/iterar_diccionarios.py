diccionario = {
    "nombre" : "lucas",
    "apellido" : "Dalto",
    "subs" : 1000000
}

#recorriendo diccionarios para obtener las keys.
for key in diccionario.items():
    print(f"la clave es: {key}")

#recorriendo diccionarios con items() para obtener la clave ey el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")