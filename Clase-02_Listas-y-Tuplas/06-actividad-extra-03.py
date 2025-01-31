# A partir del ejercicio anterior, desarrolla un programa para calcular la nota final. Para ello
# vamos a suponer que cada número es una nota y que queremos obtener la nota media. Cada
# nota tiene un valor porcentual:

# La primera nota vale un 15% del total
# La segunda nota vale un 35% del total
# La tercera nota vale un 50% del total

# Ejemplos:
# nota_1 = 10
# nota_2 = 7
# nota_3 = 4

# Solución:

nota_1 = 9
nota_2 = 3
nota_3 = 6

media = (nota_1 + nota_2 + nota_3) / 3

print(media)

nota_porcentual_1 = media * 0.15
nota_porcentual_2 = media * 0.35
nota_porcentual_3 = media * 0.5

print(nota_porcentual_1)
print(nota_porcentual_2)
print(nota_porcentual_3)