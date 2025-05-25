# Mi Resolución:
# --------------

edad = int(input("Ingrese su edad: "))
antiguedad = int(input("Ingrese su antigüedad en el sistema financiero: "))
ingreso = int(input("Ingrese su ingreso mensual en dólares: "))

if edad < 18:
    print("No tiene la edad suficiente para solicitar un crédito.")
elif antiguedad < 3:
    print("No tiene la antigüedad suficiente para solicitar un crédito.")
    if ingreso >= 4000:
        print("Puede solicitar un credito.") 
elif ingreso <= 2500:
    print("No tiene el ingreso suficiente para solicitar un crédito.")
else: print("Puede solicitar un crédito.")
    # Fin del Programa

# Resolución Clase:
# -----------------

edad = 15
antiguedad = 10
ingreso = 50000

if edad >= 18:
    if antiguedad >= 3 and ingreso >= 2500: print("Aprobado")
    elif ingreso >= 4000: print("Aprobado")
    else: print("No aprobado")
else:
    print("No aprobado")