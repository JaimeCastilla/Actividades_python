# Actividad 9: Intentos de acceso con contraseña
# Permite 3 intentos para introducir la contraseña correcta.

# Defino la contraseña correcta
contraseña_correcta = "password"

# Contador para llevar el registro de intentos fallidos
intentos = 0

# Defino el máximo número de intentos permitidos
max_intentos = 3

# Uso un bucle while para repetir el proceso mientras no se alcance el máximo de intentos
# La condición intentos < max_intentos asegura que el bucle se ejecute máximo 3 veces
while intentos < max_intentos:
    # Pido la contraseña al usuario
    contraseña = input("Introduce la contraseña: ")
    
    # Comparo la contraseña introducida con la correcta
    if contraseña == contraseña_correcta:
        print("Acceso permitido.")
        break  # El break sale del bucle inmediatamente
    else:
        # Si la contraseña es incorrecta, incremento el contador
        # intentos += 1 es equivalente a intentos = intentos + 1
        intentos += 1
        
        # Compruebo si aún quedan intentos disponibles
        if intentos < max_intentos:
            # Muestro los intentos restantes
            print(f"Contraseña incorrecta. Intentos restantes: {max_intentos - intentos}")
        else:
            # Si se agotaron los intentos, bloqueo el acceso
            print("Acceso bloqueado.")