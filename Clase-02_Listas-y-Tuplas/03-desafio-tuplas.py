# Descripción de la actividad. 
# A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente:
# 1. El último ítem de tupla
# 2. El número de ítems de tupla
# 3. La posición donde se encuentra el ítem 87 de tupla
# 4. Una lista con los últimos tres ítems de tupla
# 5. Un ítem que haya en la posición 8 de tupla
# 6. El número de veces que el ítem 7 aparece en tupla

# Copia esta tupla para iniciar el ejercicio:

tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

# SOLUCIÓN:

item_1 = tupla[-1]
print(item_1)

item_2 = len(tupla)
print(item_2)

item_3 = tupla.index(87)
print(item_3)

item_4 = tupla[-3:]
print(item_4)

item_5 = tupla[8]
print(item_5)

item_6 = tupla.count(7)
print(item_6)