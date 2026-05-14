# Programa que pide números hasta que el usuario escriba 0 y muestra la suma total

suma = 0
while True:
    numero = float(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print(f"La suma total es: {suma}")