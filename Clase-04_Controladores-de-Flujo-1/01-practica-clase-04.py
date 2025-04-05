# IF, ELIF, ELSE con Copilot:
# ---------------------------

# Copilot:
# Date: 2025-03-05
# Description: Example of using if statement in Python with CoPilot
# Version: 1.0 
# Creator: Julián Gabriel Zayas
# Example of using if statement in Python

# Define a variable
number = 10

# Check if the number is positive
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# Practica de la clase 04:
# ------------------------

# Bucle If sin validación:
# ------------------------
print("Bucle If sin validación:")
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Soy un adulto.")
else:
    print("Soy un menor de edad.")

# Bucle If con validación:
# ------------------------
print("Bucle If con validación:")
edad = int(input("Ingrese su edad: "))
if edad < 0:
    print("Edad válida.")
elif edad >= 18:
    print("Soy un adulto.")
else:
    print("Soy un menor de edad.")

# Bucle If con Casteo:
# --------------------
import sys
print("Bucle If con Casteo:")
edad = input("Ingrese su edad: ")
if not edad.isnumeric():
    print("Por favor ingrese su numero valido: ")
    sys.exit()

# Casteo de la variable edad a entero
edad = int(edad)
if edad < 0:
    print("Edad válida.")
elif edad >= 18:
    print("Soy un adulto.")
else:
    print("Soy un menor de edad.")

# Bucle If en una sola linea ejemplos:
# ------------------------------------
print("Bucle If en una sola linea ejemplos:")

# Ejemplo-1:
a = 150
b = 35
if a > b: print("a es mayor que b")

# Ejemplo-2:
a = 50
b = 150
print("A") if a > b else print("B")

# Ejemplo-3:
a = 150
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Ejemplo-4:
if edad < 0: print("Ingresose un numero valido.")
# Se imprira si es mayor de edad
print("A") if 0 > 1 else print("B")

# Ejemplo Multiples Elif:
# -----------------------
comando = "SALIR"
if comando == "ENTRAR":
    print("Bienvenido al sistema.")
elif comando == "SALUDO":
    print("Hola, ¿Cómo estás?")
elif comando == "SALIR":
    print("Saliendo del sistema.")
else:
    print("No se reconoce el comando.")


