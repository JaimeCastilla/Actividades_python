# Actividad 15: Lista numerada de programas instalados
# Muestra una lista de programas con números de índice.

# Creo una lista con varios programas predefinidos
# Los elementos están entre corchetes y separados por comas
programas = [
    "Navegador",
    "Editor de texto",
    "Antivirus",
    "Reproductor multimedia",
    "Compresor de archivos"
]

# Muestro el encabezado
print("--- Programas instalados ---")

# Uso enumerate() para obtener tanto el índice como el valor
# enumerate(programas, 1) comienza la numeración desde 1 en lugar de 0
for i, programa in enumerate(programas, 1):
    # i es el número (1, 2, 3...) y programa es el nombre del programa
    print(f"{i}. {programa}")