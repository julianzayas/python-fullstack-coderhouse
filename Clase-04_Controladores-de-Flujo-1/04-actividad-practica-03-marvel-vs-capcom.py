# Ejercicio Mavel vs Capcom
# -------------------------

nombre = input("¿Cual es tu nombre? ")
preferencia = input("Cual es tu preferencia Marvel(M) o Capcom(C): ")

if(nombre < "M" and preferencia == "M") or (nombre > "N" and preferencia == "C"):
    print("Eres del Grupo A")
else:
    print("Eres del Grupo B")

# Resolución Clase:
# -----------------

#Marvel vs Capcom
nombre = input("¿Cómo te llamas?: ")
fan = input("¿Cuál es tu preferencia (Marvel o Capcom)?: ")
if (fan == "Marvel" and nombre < "M") or (fan == "Capcom" and nombre > "N"):
  print("SOS DEL GRUPO A")
else: 
  print("Sos del epico grupo B!!!!!!!!!")