# La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila el
# cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de
# modificar las sumas incorrectas utilizando la técnica del slicing?

# Ayuda: La función llamada sum(lista) devuelve una suma de todos los elementos de la lista.

# Partirás de:
#   matriz = [
#   [1, 5, 1],
#   [2, 1, 2],
#   [3, 0, 1],
#   [1, 4, 4]
#   ]

# Debes llegar a:
#   matriz = [
#   [1, 5, 1, 7],
#   [2, 1, 2, 5],
#   [3, 0, 1, 4],
#   [1, 4, 4, 9]
#   ]

# SOLUCIÓN CHAT-GPT:

# Matriz inicial
matriz = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

# Modificar la matriz para que el cuarto elemento sea la suma de los tres primeros en cada fila
for fila in matriz:
    suma = sum(fila[:3])  # Sumar los tres primeros elementos de cada fila
    fila.append(suma)  # Agregar el cuarto elemento

# Resultado
print(matriz)

# <---------->

# SOLUCIÓN PROFESOR:
# -----------------

matriz_x = [
    [1, 2, 3, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 5]
]

# matriz[posición][columna]

matriz_x[0][-1] = sum[matriz_x[0][:-1]]

# Explicación:
# ------------
# parte_1 = parte_2

# parte_1
# matriz[0][-1] es similar a matriz[0][3] ; Los indices correspondientes a la lista son 0, 1, 2, 3

# parte_2
# matriz[0][:-1] -> '-1' implica que no va a tener en cuenta el ultimo valor en la suma.
# Es similar a matriz[0][:3] o [:len(matriz[0]) - 1] 

# Mejores-Prácticas:
# ------------------

x = [1, 2, 3, 3]
y = [1, 2, 3, 4]
z = [1, 2, 3, 5]

matriz_y = [x, y, z]

fila_1 = matriz_y[0]
fila_1[-1] = sum(matriz_y[0][-1])

# For-each: (for en python):
# --------------------------
# Recorrer linea por linea un archivo o un iterador.
matriz_z = [item for item in range(0, 100, 2)]
print(matriz_z)

# Generadores: Range.
# Iteradores: Strings, Listas, Tuplas.

# Pyton es un lenguaje interpretado, 
# es decir se va ejecutando linea por linea el archivo .py
# Existen librerias que empaquetan el codigo python en un ejecutable,
# por ejemplo un ddl, un ejecutable que ejecuta lo que esta por dentro.
# En el caso de proyectos realos de python se utilizan frameworks como:
# Flask, Django, FastAPI.
# Django crea un conjunto de archivos y carpetas base para poder trabajar.
# Se compila a medida de la creación y ejecución del codigo,
# y genera una aplicación en un servidor (IP:Puerto).