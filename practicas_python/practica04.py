# Actividad 4: Clasificar temperatura del procesador
# Clasifica la temperatura en tres categorías: normal, alta o peligrosa.

# Pido la temperatura al usuario
temperatura = float(input("Introduce la temperatura del procesador: "))

# Uso if-elif-else para crear múltiples condiciones
# Se evalúan en orden: si la primera es falsa, se pasa a la siguiente

if temperatura < 60:
    # Si es menor de 60, la temperatura es normal
    print("Temperatura normal.")
elif 60 <= temperatura <= 85:
    # Si está entre 60 y 85 (ambos incluidos), es alta
    # Solo se ejecuta si la primera condición fue falsa
    print("Temperatura alta.")
else:
    # Si ninguna condición anterior se cumple, es mayor de 85, así que es peligrosa
    print("Temperatura peligrosa.")