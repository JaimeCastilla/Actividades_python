# Actividad 11: Cuenta atrás de inicio del sistema
# Muestra una cuenta regresiva desde 10 hasta 1 antes de simular el inicio.

# El bucle for recorre números generados por range()
# range(10, 0, -1) significa:
#   - Empieza en 10
#   - Termina antes de 0 (el último número será 1)
#   - Decrementa de 1 en 1 (el -1 indica que baja en lugar de subir)
# Por lo tanto, genera: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

for numero in range(10, 0, -1):
    # En cada iteración, imprimo el número actual
    print(numero)

# Una vez terminada la cuenta atrás, muestro el mensaje de inicio
print("Inicio del sistema")