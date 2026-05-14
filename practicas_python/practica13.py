# Actividad 13: Suma de consumos eléctricos
# Registra y suma el consumo eléctrico de 5 componentes del ordenador.

# Creo un diccionario vacío para guardar los componentes y su consumo
# Un diccionario es como una lista de parejas: {clave: valor}
consumos = {}

# El bucle for se repite 5 veces (i toma valores 0, 1, 2, 3, 4)
for i in range(5):
    # Pido el nombre del componente (i + 1 para mostrar 1-5 en lugar de 0-4)
    nombre_componente = input(f"Introduce el nombre del componente {i + 1}: ")
    
    # Pido el consumo en vatios del componente
    consumo_vatios = float(input(f"Introduce el consumo en vatios de {nombre_componente}: "))
    
    # Guardo el componente y su consumo en el diccionario
    # nombre_componente es la clave, consumo_vatios es el valor
    consumos[nombre_componente] = consumo_vatios

# Muestro un encabezado con salto de línea (\n)
print("\n--- Lista de componentes registrados ---")

# Recorro el diccionario usando .items() para obtener clave y valor simultáneamente
for componente, consumo in consumos.items():
    print(f"{componente}: {consumo} W")

# Calculo el consumo total usando sum()
# .values() obtiene todos los valores del diccionario (los consumos)
consumo_total = sum(consumos.values())

# Muestro el resultado final
print(f"\nConsumo total del equipo: {consumo_total} W")