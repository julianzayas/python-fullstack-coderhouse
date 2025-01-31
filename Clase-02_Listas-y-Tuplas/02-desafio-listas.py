# Dadas dos listas LISTA1 y LISTA2 debes realizar las siguientes tareas:

# Añade a la LISTA1 el int 456789 y luego el string “Hola Mundo”
# Luego añade a la LISTA2 el string “Hola y Adios” y luego el int 5555
# Genera una LISTA3 con todos los elementos de la LISTA1 sin considerar el último elemento (slicing)
# Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último elemento (pop)
# Finalmente, genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3

Lista_1 = []
Lista_2 = list()

Lista_1.append(456789)
Lista_1.append("Hola Mundo")

Lista_2.append("Hola y Adios")
Lista_2.append(5555)

print(Lista_1)
print(Lista_2)

Lista_3 = []
Lista_3 = Lista_1[:-1]
print(Lista_3)

# Copia y borra los datos con Slicing
# Lista_4 = Lista_2[1:-1]

# SI SE REALIZA MEDIANTE ESTE METODOS SE MODIFICAN LOS VALORES DE LA LISTA INICIAL
# SIEMPRE ES MEJOR USAR .COPY() PARA NO MODIFICAR LA LISTA INIICIAL
# SI SE USA SLICING NO SE MODIFICA LA LISTA INICIAL
Lista_X = Lista_2

# Copia los datos de la Lista_2 en la Lista_4
Lista_4 = Lista_2.copy()
Lista_4.pop()
Lista_4.pop(0)
print(Lista_4)
print(Lista_2)

# Asignar a una lista el valor borrado de otra lista
# Lista_X = Lista_2.pop()
# print(Lista_X)

Lista_5 = []
Lista_5 = Lista_3 + Lista_4
print(Lista_5)