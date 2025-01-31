# Consigna:

# A partir de dos variables llamadas NOMBRE y EDAD, debes crear una variable que almacene si se cumplen
# todas las siguientes condiciones, encadenando operadores lógicos en una sola línea:
# NOMBRE sea diferente de cuatro asteriscos “****”
# EDAD sea mayor que 5 y a su vez menor que 20
# Que la longitud de NOMBRE sea mayor o igual a 4 pero a la vez menor que 8

# EDAD multiplicada por 3 sea mayor que 35
# Desde un input conseguir las variables:
# nombre = INPUT!!!
# edad = INPUT!!!!

# SOLUCIÓN:

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

# Validación - Julián:
variable = (nombre != "****") and (20 > edad > 5) and (8 > len(nombre) >= 4) and (edad*3 > 35)
print(variable)

# Validación - Profesor:
print((nombre != '****') and (edad > 5 and  edad < 20) and (8 >= len(nombre) >= 4) and ((edad *3) > 35))

# Validación - Buenas-Prácticas:
premisa_1 = nombre != '****'
premisa_2 = 20 > edad > 5
premisa_3 = 8 >= len(nombre) >= 4
premisa_4 = (edad * 3) > 35
print(premisa_1 and premisa_2 and premisa_3 and premisa_4)
