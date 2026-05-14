# Actividad 5: Comprobar espacio libre en disco
# Verifica si hay suficiente espacio libre en el disco (mínimo 20 GB).

# Pido los GB libres del disco duro
gb_libres = float(input("Introduce los GB libres del disco duro: "))

# Comparo el espacio disponible con el mínimo recomendado (20 GB)
# >= significa "mayor o igual a"
if gb_libres >= 20:
    # Si tiene 20 GB o más, hay espacio suficiente
    print("Hay espacio suficiente.")
else:
    # Si tiene menos de 20 GB, debería liberar espacio
    print("Conviene liberar espacio.")