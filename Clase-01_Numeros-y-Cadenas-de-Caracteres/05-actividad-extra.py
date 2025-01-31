# Mi primer programa en Python

# Consigna:

# Trabajas en Coderhouse y te piden crear un programa que calcule la nota final de estudiantes del curso de Python. La nota final se calcula basándonos en tres notas previas de las cuales, cada una corresponde un porcentaje distinto de la nota final. Los porcentajes se detallan a continuación:

# Los porcentajes asociados que debemos considerar de cada nota se detallan a continuación: 
# nota_1 cuenta como el 20% de la nota final
# nota_2 cuenta como el 30% de la nota final
# nota_3 cuenta como el 50% de la nota final

# Aspectos a incluir:
# Tener en cuenta los temas vistos en la clase 1: números, print, input, variables, operaciones matemáticas, cadena de texto. 
# Los datos deben guardarse en variables y deben ser dinámicos por medio de input.

# SOLUCIÓN:

nota_1 = int(input("Ingrese la primera nota del alumno: "))
nota_2 = int(input("Ingrese la segunda nota del alumno: "))
nota_3 = int(input("Ingrese la tercera nota del alumno: "))

nota_final = nota_1 * 0.2 + nota_2 * 0.3 + nota_3 * 0.5
print(nota_final)
