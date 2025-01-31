print(not 3)
print(False == 5)

# Ejercicio:
print("Expresiones:")
expresiones = [
    not False,
    not 3 == 5, # Prioridad Algebraica ; 0 o None (vacio) es False.
    33/3 == 11 and 5 > 2,
    True or False,
    True*5 == 2.5*2 or 123 >= 23, # 1*5 == 2.5*2
    12 > 7 and True < False
    ]
print(expresiones)