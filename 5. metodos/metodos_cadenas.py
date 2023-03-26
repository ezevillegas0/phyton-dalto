#metodos de cadena. funciones aplicadas a objetos.

cadena1 = "hola soy dalto"
cadena2 = "bienvenido maquinola"

# DIR - devuelve la lista de atributos del objeto pasado. mas que un metodo es considerado una funcion.
resultado = dir(cadena1)

#----------------------------------#

# UPPER - convierte a mayuscula.
resultado2 = cadena1.upper()
resultado3 = "hola mostro".upper()
# LOWER - convierte a minuscula.
resultado4 = "HOLA COMO TE VA".lower()
# CAPITALIZE - primera en mayuscula convirtiendo todo a minuscula.
resultado5 = cadena1.capitalize()

#----------------------------------#

#FIND - busca y encuentra la primera aparicion del valor especificado, si no devuelve -1.
busqueda_find = cadena1.find("hola")
# INDEX - metodo encuentra la primera aparicion del calor especificado, sino devuelve una excepsion.
busqueda_index = cadena1.index("d")

#----------------------------------#

# ISNUMERIC - si es numerico devuelve true.
es_numerico = cadena1.isnumeric()
# ISALPHA - si es alfa numerico devuelve true.
es_alafanumerico = cadena1.isalpha()

#----------------------------------#

# COUNT - devuelve el numero de ocurrencias de una subcadena en la cadena dada.
contar_coincidencias = cadena1.count("a")
# LEN - cuenta los caracteres de una cadena. esta es considerada como una funcion.
contar_carcters = len(cadena1)

#----------------------------------#

# ENDSWITH - verifica si una cadena comienza con otra cadena dada. si es asi, devuelve true.
empieza_con = cadena1.startswith("hola")
# STARTSWITH - verifica si una cadena termina con otra cadena dada. si es asi, devuelve true.
termina_con = cadena1.endswith("dalto")

#----------------------------------#

# REPLACE - reemplaza un valor por otro.
cadena_nueva = cadena1.replace("hola" , "hi") 
# SPLIT - separa por el parametro dado. devuelve una lista.
cadena3 = "hola,maquinola,como,estas?"
cadena_separada = cadena3.split(",")

print(cadena_separada)
