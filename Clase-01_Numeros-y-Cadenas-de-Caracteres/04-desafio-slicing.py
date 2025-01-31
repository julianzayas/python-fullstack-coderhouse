# Se tiene una cadena de texto, pero al revés. Al parecer contiene el nombre de un alumno, la nota de un examen y la materia. 

# De forma individual, realiza lo siguiente: 

# 1. Dar vuelta la cadena y asignarla a una variable llamada cadena_volteada. Para devolver una cadena dada vuelta se usa el tercer índice negativo con slicing: cadena[::-1]. 
# 2. Extraer nombre y apellido, almacenarlo en una variable llamada nombre_alumno.
# 4. Extraer la nota y almacenarla en una variable llamada nota.
# 5. Extraer la materia y almacenarla en una variable llamada materia. 
# 6. Mostrar por pantalla la siguiente estructura: 

# NOMBRE APELLIDO ha sacado un NOTA en MATERIA

# SOLUCIÓN:

# Slicing
# -------
# Valores por defecto -> [donde-inicia:donde-finaliza:cantidad-saltos]
# [::] equivale a [0:len(sting):1]
# No es necesario el último valor

# Ejemplo
palabra_1 = "Python"
palabra_2 = palabra_1[::-1]
print(palabra_2)

# Movimientos previos
cadena_inicial = "Julián Zayas ha sacado un 10 en Algoritmos"
cadena_volteada = cadena_inicial[::-1]
print(cadena_volteada)

# Ordenar cadena
cadena_ordenada = cadena_volteada[::-1]
print(cadena_ordenada)

# Slicing
nombre_alumno = cadena_ordenada[:12:]
print(nombre_alumno)
nota = cadena_ordenada[26:28:]
print(nota) 
materia = cadena_ordenada[32::]
print(materia)

# Estructura final
print(nombre_alumno + " ha sacado un " + nota + " en " + materia)