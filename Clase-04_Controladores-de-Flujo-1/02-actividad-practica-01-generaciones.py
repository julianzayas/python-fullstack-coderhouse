# Actividad Práctica 01 - Generaciones Digitales:
# -----------------------------------------------

anio_nac = int(input("Ingrese el año de su nacimiento: "))
if 1920 <= anio_nac <= 1940: print("Usted pertenece a la Generación Silenciosa.")
elif 1946 <= anio_nac <= 1964: print("Usted pertenece a la Generación Baby Boomer.")
elif 1965 <= anio_nac <= 1979: print("Usted pertenece a la Generación X.")
elif 1980 <= anio_nac <= 2000: print("Usted pertenece a la Generación Y (Millennials).")
elif 2001 <= anio_nac <= 2010: print("Usted pertenece a la Generación Z.")
else: print("Usted pertence a una generación no clasificada.")  
