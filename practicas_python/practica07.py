# Actividad 7: Menú de mantenimiento básico
# Muestra un menú de opciones y ejecuta acciones según la selección del usuario.

# Muestro las opciones disponibles del menú
print("Menú de mantenimiento básico:")
print("1. Comprobar disco.")
print("2. Comprobar memoria RAM.")
print("3. Comprobar temperatura.")
print("4. Salir.")

# Pido al usuario que seleccione una opción y convierto a número entero
opcion = int(input("Elige una opción (1-4): "))

# Uso múltiples condiciones if-elif para procesar cada opción
# El programa comprueba cada número y ejecuta la acción correspondiente

if opcion == 1:
    # Si elige 1, muestra un mensaje sobre la comprobación del disco
    print("Comprobando disco...")
elif opcion == 2:
    # Si elige 2, muestra un mensaje sobre la comprobación de RAM
    print("Comprobando memoria RAM...")
elif opcion == 3:
    # Si elige 3, muestra un mensaje sobre la comprobación de temperatura
    print("Comprobando temperatura...")
elif opcion == 4:
    # Si elige 4, muestra un mensaje de salida
    print("Saliendo...")
else:
    # Si introduce cualquier otro número, muestra un mensaje de error
    print("Opción no válida.")