# Actividad 3: Comprobar temperatura válida
# Valida que una temperatura esté dentro del rango permitido (0-110 grados).

# Pido la temperatura al usuario y la convierto a float (número decimal)
# Uso float en lugar de int para permitir temperaturas como 65.5
temperatura = float(input("Introduce la temperatura del procesador: "))

# Uso una estructura condicional if-else para comprobar el rango
# La expresión 0 <= temperatura <= 110 verifica que esté entre 0 y 110 (ambos incluidos)
if 0 <= temperatura <= 110:
    print("La temperatura es válida.")
else:
    print("La temperatura no es válida.")