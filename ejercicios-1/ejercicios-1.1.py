#promedio de duraciones de los cursos
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencia de duracion con los otros cursos.
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso  * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando el porcentaje de tiempo vaciado removido.
tiempo_vacio_promedio = 100 - otros_cursos_promedio  * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso  * 1000 // crudo_dalto / 10

#mostrando las diferencias de duracion
print(f"El curso de dalto dura un {diferencia_con_min}% menos que el mas rapido")
print(f"El curso de dalto dura un {diferencia_con_max}% menos que el mas largo")
print(f"El curso de dalto dura un {diferencia_con_promedio}% menos que el promedio")

#mostrando la cantidad de espacios vacios que se remueven
print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio.")
print(f"este curso elimino {tiempo_vacio_dalto}% de tiempo vacio.")

#mostrando diferencias si los cursos duraran 10 horas.
print(f'ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de este curso')