contador = 0

palabra = input("Ingrese una palabra, 'fin' para terminar: ")
while palabra != "fin":
    contador += 1
    palabra = input("Ingrese otra palabra, 'fin' para terminar: ")
print(f"La cantidad de palabras ingresadas es: {contador}")