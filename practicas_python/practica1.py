# Actividad 1: Descripción del ordenador
# Pido datos del ordenador al usuario y luego los muestro en una frase.

# Pido al usuario la marca del PC
automarca = input("Dime la marca de tu PC: ")

# Pido al usuario el modelo del PC
modelo = input("Dime el modelo de tu PC: ")

# Pido al usuario el tipo de equipo (por ejemplo, sobremesa o portátil)
tipo_equipo = input("Dime el tipo de tu PC: ")

# Muestro los datos recopilados en una sola frase usando un f-string
# Un f-string permite incluir las variables directamente dentro del texto
print(f"Tu PC es una {automarca} modelo {modelo} y es un {tipo_equipo}")