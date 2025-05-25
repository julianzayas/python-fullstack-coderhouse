# Ejercicio Mavel vs Capcom
# -------------------------

nombre = input("¿Cuál es tu nombre?: ")
preferencia = input("Cuál es tu preferencia Marvel(M) o Capcom(C): ")
if(nombre < "M" and preferencia == "M") or (nombre > "N" and preferencia == "C"):
    print("Eres del Grupo A")
else:
    print("Eres del Grupo B")

# Resolución Clase:
# -----------------

#Marvel vs Capcom
nombre = input("¿Cuál es tu nombre?: ").upper()
pref = input("¿Cuál es tu preferencia, Marvel(M) o Capcom(C)?: ").upper
# Validación:
if pref not in ["M", "C"]: # Lista
  print("No es una preferencia válida")
else:
  if (pref == "M" and nombre[0] < "M") or (pref == "C" and nombre[0] > "N"):
    print("SOS DEL GRUPO A")
  else:
    print("Sos del epico grupo B!!!!!!!!!")

