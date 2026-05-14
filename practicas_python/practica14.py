# Actividad 14: Lista de periféricos
# Solicita 5 periféricos y los almacena en una lista.

# Creo una lista vacía para guardar los periféricos
# Las listas se crean con corchetes [] y almacenan elementos en orden
perifericos = []

# El bucle for se repite 5 veces
for i in range(5):
    # Pido el nombre de cada periférico
    periferico = input(f"Introduce el periférico {i + 1}: ")
    
    # Agrego el periférico a la lista usando .append()
    # append() añade un elemento al final de la lista
    perifericos.append(periferico)

# Muestro un encabezado
print("\n--- Periféricos introducidos ---")

# Recorro la lista mostrando cada periférico
for periferico in perifericos:
    print(periferico)