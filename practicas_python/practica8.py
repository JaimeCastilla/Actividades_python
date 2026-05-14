# Actividad 8: Comprobar usuario permitido
# Valida que el usuario introducido sea el autorizado (admin).

# Guardo el nombre de usuario permitido en una variable
# Así puedo cambiar fácilmente el usuario autorizado si es necesario
usuario_permitido = "admin"

# Pido al usuario que escriba su nombre de usuario
# El método .strip() elimina espacios en blanco al inicio y final
# Esto evita errores si el usuario escribe " admin " por accidente
usuario = input("Introduce tu nombre de usuario: ").strip()

# Comparo el usuario introducido con el usuario permitido usando ==
if usuario == usuario_permitido:
    # Si coincide, muestro acceso permitido
    print("Acceso permitido.")
else:
    # Si no coincide, muestro acceso denegado
    print("Acceso denegado.")