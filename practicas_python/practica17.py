# Actividad 17: Lista de diccionarios de ordenadores
# Registra información de varios ordenadores en una estructura de datos compleja.

# Creo una lista vacía que contendrá varios diccionarios (uno por ordenador)
ordenadores = []

# Bucle que permite registrar múltiples ordenadores
while True:
    # Pido la marca del ordenador
    # .strip() elimina espacios al inicio y final
    marca = input("Introduce la marca del ordenador (o 'fin' para terminar): ").strip()
    
    # Si escribió "fin", termino el registro
    if marca.lower() == "fin":
        break
    
    # Pido los datos del ordenador
    modelo = input("Introduce el modelo: ").strip()
    ram = input("Introduce la memoria RAM (GB): ").strip()
    disco = input("Introduce la capacidad de disco (GB): ").strip()
    so = input("Introduce el sistema operativo: ").strip()
    
    # Creo un diccionario con los datos del ordenador
    # Las claves son los nombres de los campos (marca, modelo, etc.)
    # Los valores son los datos introducidos por el usuario
    ordenador = {
        "marca": marca,
        "modelo": modelo,
        "ram": ram,
        "disco": disco,
        "so": so
    }
    
    # Agrego el diccionario del ordenador a la lista
    ordenadores.append(ordenador)

# Muestro todos los ordenadores registrados
print("\n--- Ordenadores registrados ---")

# Uso enumerate para obtener el número y el diccionario de cada ordenador
for i, ordenador in enumerate(ordenadores, 1):
    print(f"\nOrdenador {i}:")
    # Accedo a cada valor del diccionario usando las claves entre comillas
    print(f"  Marca: {ordenador['marca']}")
    print(f"  Modelo: {ordenador['modelo']}")
    print(f"  RAM: {ordenador['ram']} GB")
    print(f"  Disco: {ordenador['disco']} GB")
    print(f"  Sistema Operativo: {ordenador['so']}")