# Actividad 12: Conversión de GB a MB
# Convierte gigabytes a megabytes usando la equivalencia 1 GB = 1024 MB.

# Pido al usuario que introduzca la cantidad de GB
# Uso float para permitir valores como 2.5 GB
gb = float(input("Introduce la cantidad de GB: "))

# Realizo la conversión multiplicando por 1024
# 1 GB = 1024 MB, así que 2 GB = 2 * 1024 = 2048 MB
mb = gb * 1024

# Muestro el resultado usando f-strings para insertar ambos valores
print(f"{gb} GB equivalen a {mb} MB")