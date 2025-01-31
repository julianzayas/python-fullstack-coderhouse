# Practicas en Python
# Curso Fullstack Codo a Codo
# ---------------------------
# Clase-02
# los String funcionan de forma similar a las Listas

nombre = "Julián Gabriel Zayas"

# Slicing de String
print(nombre[::-1]) # 1. donde inicia, 2. donde finaliza, 3. cantidad de saltos
print(nombre[::2])
print(nombre[:5])
print(len(nombre))

# LISTAS
# ------
# Son Arrays Mutables

nombre_lista = ["J", "u", "l", "i", "á", "n", " ", "G"]
print(nombre_lista)

# Slicing funciona con Listas
print(nombre_lista[::-1])
print(nombre_lista[::2])
print(nombre_lista[:5])

# Longintud de Lista
print(len(nombre_lista))

# Concatenación de Lista
numeros = [1, 2, 3, 4, 5]
print(numeros + [6, 7, 8, 9])

# Las Listas son Mutables, los String no
# nombre[4] = "a"
# print(nombre)
nombre_lista[4] = "a"
print(nombre_lista)

# Asignación por Slicing
letras = ["a", "b" , "c", "d" , "e", "f"]
letras[:3] = ["A", "B", "C"]
print(letras)

# La reasignación en otros lenguajes es por el mismo tipo de dato.
# En Python se puede reasignar por cualquier tipo de dato.

# Borrado por Slicing (segmento,definir segmento)
# Ejemplo: Borrar los 3 primeros valores de la lista (asignar lista vacía)
letras[:3] = []
print(letras)

# Ejemplo: Borrar nombres de una Lista
nombre_completo = ["J", "u", "l", "i", "á", "n", " ", "G", "a", "b", "r", "i", "e", "l"]
print(nombre_completo)
# Primer nombre - metodo 1
nombre_completo[6:] = []
print(nombre_completo)
# Segundo nombre - metodo 2
# nombre_completo_borrado = nombre_completo[7:]
# print(nombre_completo_borrado)

# Números pares
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros_pares = numeros[::2]
print(numeros_pares)

# Borrar valores de Lista
letras_1 = ["a", "b", "c", "d"]
letras_1 = []
print(letras_1)

# Inicializar Listas: 2 Formas
# ---------------------------
list_1 = list() # 0.03 ms
list_2 = [] # 0.01 ms

# Funciones Integradas

# Función Append
# --------------
# Agregar al final de la lista
list_2.append(5)
print(list_2)

# Integrar funciones matemáticas con Append
# Forma simple
list_2.append(3*2)
print(list_2)
# Forma legible
numero_multiplicado = 4*3
list_2.append(numero_multiplicado)
print(list_2)

# Ingreso por Input
list_2.append(input("Ingrese un numero para agregar a la lista: "))
print(list_2)

# Longitud de lista
print(len(list_2))

# Función Pop 
# -----------
# Por defecto elimina el ultimo valor de la lista
# Podemos especificar la posición de la cual queremos extrar el valor

datos = [1, -5, 123, 34, 'Una cadena', 'Otra cadena']
print(datos)

datos.pop(4)
print(datos)

# Valor por defecto (-1)
datos.pop()
print(datos)

# Función Count
# -------------
# Cuantas veces aparece un número o string en una lista

numeros_2 = [1, 2, 1, 3, 1, 4, 1]
print(numeros_2)
print(numeros_2.count(1))

# Función Index
# -------------
# Indica en que posición se encuentra un valor

numeros_3 = [1, 2, 1, 3, 1, 4, 1, 5]
print(numeros_3.index(5))

# Si no existe en la lista devuelve error

# Si existe más de una ocurrencia, devuelve el indice de la primera
print(numeros_3.index(1))

# TUPLAS
# ------
# Arrays Inmutables
# Se pueden escribir con parentesis por convención, pero no es necesario.

mi_tupla = (1,2,3,4)
mi_tupla_2 = 1,2,3,4
print(type(mi_tupla_2))

tupla_vacia = 2,
# Es una Tupla por la coma
tupla_vacia = 2
# Es un Int por no llevar la coma

# Longitud de la Tupla
print(len(mi_tupla))

# Ejemplos
Tupla_1 = 2,
print(type(Tupla_1))

Tupla_2 = 2, 3, 4
print(type(Tupla_2))

# Asignación en la tupla -> Error
# mi_tupla[1] = 1

# Las Tuplas se utilizan para guardar por ejemplo valores de conezión a bases de datos
# Las Tuplas brindan mayor seguridad al no poder ser modificadas

# Slicing en Tuplas
Tupla_3 = Tupla_2[:-1]
print(Tupla_3)

# LISTAS DE TUPLAS
# ----------------

Lista_1 = list(Tupla_2)
print(Lista_1)

# Casteo de Tuplas
str_1 = str(Tupla_2)
print(Tupla_2)
print(type(str_1))

# Count de Tuplas
Tupla_4 = 1, 4, 8, 1
print(Tupla_4.count(1))

# Index de Tuplas
print(Tupla_4.index(4))

# Lista Anidada (Lista dentro de otra lista)
datos = [155, [2,3,4], 'Una Cadena', 'Otra Cadena']
# Tupla Anidad (Tupla dentro de otra tupla)
otros_datos = (2, (5, 6, 7), 1, 8)

# Anidación de Tupla<->Lista Lista<->Tupla
lista_con_tupla = [1, (2, 3, 4), 'Una Cadena', 'Otra Cadena']
tupla_con_lista = (2, [5, 6, 7], 1, 8)

# Transformacíon de colecciones
numeros = (1, 2 ,3 , 4)
numeros = list(numeros)
print(numeros)

letras = ['a', 'b', 'c', 'd']
letras = tuple(letras)
print(letras)

# No tiene sentido modificar tupla a lista, ya que la tupla se usa para seguridad

# Tupla vacia
tupla_vacia = ()
print(tupla_vacia)
print(type(tupla_vacia))

# Otra forma 
tupla_vacia_2 = None # Similar a Null