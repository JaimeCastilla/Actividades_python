# Actividad 20: Saludo personalizado con control de errores
# Define una función que saluda al usuario de forma personalizada.

# Defino una función que recibe el nombre como parámetro
def saludar_alumno(nombre):
    # Muestro un saludo personalizado usando f-strings para insertar el nombre
    print(f"¡Hola, {nombre}! Bienvenido a la práctica de Python.")

# Pido el nombre al usuario
# .strip() elimina espacios al inicio y final de la entrada
nombre = input("Introduce tu nombre: ").strip()

# Compruebo si el nombre está vacío
if nombre == "":
    # Si está vacío, muestro un mensaje de error
    print("Error: El nombre no puede estar vacío.")
else:
    # Si no está vacío, llamo a la función pasando el nombre como argumento
    saludar_alumno(nombre)