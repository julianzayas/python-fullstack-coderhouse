# Operadores Logicos y Expresiones Anidadas

# Comparación de strings, distingue mayusculas de minusculas
texto1 = 'hola'
texto2 = 'Hola'
print(texto1 == texto2)
# False

print(texto1 > texto2)
# True: Por el valor de los caracteres ASCII
print([ord(c) for c in texto1])
print([ord(c) for c in texto2])
# h en ASCII = 104
# H en ASCII = 72

# Operador "Diferente"
print(texto1 != texto2)
# True

# Operador "Negación"
print(not(texto1 == texto2))
# True: Niega el resultado de la expresión entre parentesis.

# Uno caso particular que sucede en buclues if o elses
# Es que se busca que no entre a hacer las acciones cuando sea verdadero
# En estos casos es util el operador "Negación"

# OPERADORES LÓGICOS:
# -------------------

print("Uso de Operadores Lógicos")
print("Operador OR:")
print(10 >= 8)
print(10 > 8 or 10 == 8) # True OR False -> 1 OR 0 = 1 (Tabla de Verdad)
print(10 > 8 and 10 == 8) # True AND False -> 1 AND 0 = 0

# OR da verdadero si alguno es verdadero, en otro caso es falso # DISYUNCIÓN
# Velocidad en Python: Si la primera da True no verifica la segunda expresión

print("Ejemplo prioridad de comprobación con peligros en python:")
print(True or 1/0) # 1/0 -> Error
# True -> Cuidado!

print("Ejemplo de busqueda de True con OR con error valores False y error")
# OR busca hasta encontrar True para validar, en este caso el primer valor es False y el segundo error
# por lo tanto muestra el error, ya que no encontro ningun valor True.
# print(False or 1/0)
# Error!

print("Operador AND:")
print(True and False)
# AND da falso si alguno es falso, en otro caso es verdadero # CONJUNCIÓN

# De la misma forma que en OR, si el operador AND encuentra un valor False antes que un error
# u otros valores posibles (True), entonces muestra como resultado False.
print("Tratamiento de la prioridad de verificación de False con operador AND")
(False and 1/0)
# Funciona por prioridad de AND!

print("Tratamiento de errores con AND:")
# print(True and 1/0)
# Error! Si es verdadero, tiene que verificar la segunda para confirmar si es True o no.

# EN OCASIONES SE DEBEN Y SE PUEDEN VERIFICAR TODAS LAS EXPRESIONES ANTES DE DAR EL RESULTADO.

# OPERADORES DE ASIGNACIÓN:
# -------------------------
print("OPERADORES DE ASIGNACIÓN:")
# Necesitan una variable previamente declarada.

# Asigación: Asignar valor "="

# Suma en asignación:
# Tambien funciona en Strings.
print("Suma en Asginación:")
a = 0
a += 1
print(a)

# Funciona con todos los operadores aritméticos salvo algunos casos: Exponenciación en String.
# Se pueden usar en enteros y flotantes.
# -=; *=; /=; %= (modulo); **= (exponente).

# Super-Asignación:
print("Super-Asignación:")
texto = 'hola'
texto += ' mundo' # texto = texto + " mundo"
print(texto)
