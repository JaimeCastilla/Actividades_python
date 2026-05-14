# Actividad 6: Clasificar memoria RAM
# Clasifica la memoria RAM en tres niveles: baja, media o alta.

# Pido la cantidad de RAM al usuario y la convierto a número entero
ram_gb = int(input("Introduce la cantidad de memoria RAM en GB: "))

# Creo una cadena de condiciones para clasificar la RAM
# Cada rango representa una categoría diferente de rendimiento

if ram_gb < 8:
    # Menos de 8 GB es considerado bajo
    print("Memoria baja.")
elif 8 <= ram_gb <= 15:
    # Entre 8 y 15 GB (ambos incluidos) es medio
    print("Memoria media.")
else:
    # 16 GB o más es considerado alto
    print("Memoria alta.")