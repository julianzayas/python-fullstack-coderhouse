# Desarrollar un programa que permita calcular el promedio final de los equipos de futbol en un torneo.

# Condiciones:

# Jugaron 20 partidos durante el torneo.
# Los partidos poseen diferente puntaje según el resultado, los partidos ganados 3 puntos, partido empatado 1 punto, partido perdido 0 puntos.
# El promedio final resulta de la cantidad de puntos totales divididos la cantidad de partidos.

#La cantidad de partidos que debemos considerar a un equipo para el ejemplo se detallan a continuación: 

# partidos_ganados 8
# partido_empatados 7
# partido_perdidos 5

# Importante: Cada una de las cantidades de partidos ganados, empatados o perdidos debe solicitarse al usuario utilizando la función input().

# SOLUCIÓN:

# Equipo_1
partidos_ganados_equipo_1 = int(input("Ingrese la cantidad de partidos ganados del equipo 1: "))
partidos_empatados_equipo_1 = int(input("Ingrese la cantidad de partidos empatados del equipo 1: "))
partidos_perdidos_equipo_1 = int(input("Ingrese la cantidad de partidos perdidos del equipo 1: "))

# Equipo_2
partidos_ganados_equipo_2 = int(input("Ingrese la cantidad de partidos ganados del equipo 2: "))
partidos_empatados_equipo_2 = int(input("Ingrese la cantidad de partidos empatados del equipo 2: "))
partidos_perdidos_equipo_2 = int(input("Ingrese la cantidad de partidos perdidos del equipo 2: "))

# Equipo_3
partidos_ganados_equipo_3 = int(input("Ingrese la cantidad de partidos ganados del equipo 3: "))
partidos_empatados_equipo_3 = int(input("Ingrese la cantidad de partidos empatados del equipo 3: "))
partidos_perdidos_equipo_3 = int(input("Ingrese la cantidad de partidos perdidos del equipo 3: "))

# Calculo de puntos por equipos
puntos_ganados_equipo_1 = partidos_ganados_equipo_1 * 3
puntos_empatados_equipo_1 = partidos_empatados_equipo_1 * 1
total_puntos_equipo_1 = puntos_ganados_equipo_1 + puntos_empatados_equipo_1
print(total_puntos_equipo_1)
   
puntos_ganados_equipo_2 = partidos_ganados_equipo_2 * 3
puntos_empatados_equipo_2 = partidos_empatados_equipo_2 * 1
total_puntos_equipo_2 = puntos_ganados_equipo_2 + puntos_empatados_equipo_2
print(total_puntos_equipo_2)

puntos_ganados_equipo_3 = partidos_ganados_equipo_3 * 3
puntos_empatados_equipo_3 = partidos_empatados_equipo_3 * 1
total_puntos_equipo_3 = puntos_ganados_equipo_3 + puntos_empatados_equipo_3
print(total_puntos_equipo_3)

# Calculos finales
total_puntos_global = total_puntos_equipo_1 + total_puntos_equipo_2 + total_puntos_equipo_3
print(total_puntos_global)
promedio_puntos_todos_equipos = total_puntos_global / 3
print("El promedio total de puntos de todos los equipos es: ")
print(promedio_puntos_todos_equipos)
# print("El promedio total de puntos de todos los equipos en el torneos es: " + promedio_puntos_todos_equipos)