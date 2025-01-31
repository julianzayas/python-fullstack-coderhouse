# Practicas en Python
# Curso Fullstack Codo a Codo
# ---------------------------
# Clase-01

# Función Print:
# --------------
print("Hola Mundo")
print("Segundo Hola Mundo")
print("comillas dobles dentro de \"comillas dobles\"")
# Caracter especial comilla simple
print('I don\'t like the juice')
# Print número simple
print(4)
# Dos tipos de Indentación de Strings
print("""una cadena
otra cadena
otra cadena más""")
print("una cadena\notra cadea\notra cadena más")

# Variables
# ---------
saludo = "hola"
print(saludo)
numero_negativo = -10
print(numero_negativo)
nombre = "Julián"
print(nombre)
# Mostrar Variable sin Print
nombre
# Otras variables
nombre_2 = "Pepe"
nombre_profesor = "Julián"
nombre_estudiante = "Pepe"

# Función Input:
# -------------
nombre_ingresado = input("Por favor ingrese su nombre: ")
print(nombre_ingresado)
numero_1 = input("Ingrese el primer número a sumar: ")
numero_2 = input("Ingrese el segundo número a sumar: ")

# Concatenación de números
print(numero_1 + numero_2)

# Casteo de variables dentro de función Print
print(int(numero_1) + int(numero_2))

# Concatenación y Casteo
print(int(numero_1 + numero_2))

# Casteo en el ingreso de las variables
numero_1 = int(input("ingresae el primer nímero a sumar: "))
numero_2 = int(input("ingresae el primer nímero a sumar: "))
print(numero_1 + numero_2)

# Manejo de Strings:
# ------------------

# Combinación Strings con operaciones artimética:
palabra_1 = "Julián"
print(palabra_1 * 5)
# Longitud de String:
palabra_2 = 'Python'
print(len(palabra_2))
# *Solo en Google Colab
len(palabra_2)

# Ejemplo de Slicing:
# -------------------

# Inmutabilidad de cadenas de texto
palabra_inmutable = "Pithon"
print(palabra_inmutable)
# Modificación con slicing
palabra_modificada = palabra_inmutable[0:1] + 'y' + palabra_inmutable[2:]
print(palabra_modificada)