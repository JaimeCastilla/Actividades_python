# Actividad 10: Mostrar números pares
# Muestra todos los números pares del 2 al 20 usando un bucle for.

# El bucle for recorre una serie de números generados por range()
# range(2, 21, 2) significa:
#   - Empieza en 2
#   - Termina antes de 21 (el último número será 20)
#   - Incrementa de 2 en 2
# Por lo tanto, genera: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20

for numero in range(2, 21, 2):
    # En cada iteración del bucle, 'numero' toma un valor de la secuencia (lo muestro)
    print(numero)