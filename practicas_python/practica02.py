# Actividad 2: Antigüedad de un ordenador
# Calcula cuántos años tiene un ordenador restando el año de compra al año actual.

# Importo el módulo datetime para obtener el año actual automáticamente
import datetime as datetime

# Obtengo el año actual usando datetime
# datetime.now() devuelve la fecha y hora actual
# .year extrae solo el año (2026)
año_actual = int(datetime.now().year)

# Pido al usuario el año de compra y lo convierto a número entero con int()
# Esto es necesario porque input() siempre devuelve texto
año_compra = int(input("Introduce el año de compra del ordenador: "))

# Calculo la antigüedad restando el año de compra al año actual
# Por ejemplo: 2026 - 2020 = 6 años
antiguedad = año_actual - año_compra

# Muestro el resultado usando f-strings para insertar el valor dentro del texto
print(f"El ordenador tiene aproximadamente {antiguedad} años.")