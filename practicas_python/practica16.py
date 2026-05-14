# Actividad 16: Contar incidencias informáticas
# Registra incidencias hasta que el usuario escriba "fin" y cuenta el total.

# Creo una lista vacía para guardar las incidencias
incidencias = []

# Uso un bucle while True que se repetirá indefinidamente
# hasta que encuentre un break (sentencia que interrumpe el bucle)
while True:
    # Pido al usuario que escriba una incidencia
    incidencia = input("Introduce una incidencia (o escribe 'fin' para terminar): ")
    
    # Uso .lower() para convertir a minúsculas (así "FIN" o "Fin" también funcionan)
    # Si el usuario escribió "fin", salgo del bucle
    if incidencia.lower() == "fin":
        break  # break detiene el bucle inmediatamente
    
    # Si no escribió "fin", agrego la incidencia a la lista
    incidencias.append(incidencia)

# Uso len() para contar cuántos elementos hay en la lista
print(f"\nTotal de incidencias registradas: {len(incidencias)}")