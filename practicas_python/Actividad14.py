equipos_lista = []
salida = ""

while salida != "si":
    nombre_equipo = input("Introduce el nombre del equipo: ")
    equipos_lista.append(nombre_equipo)
    salida = input("Has terminado, introduzca si para acabar: ")

print("Equipos introducidos:")
print(equipos_lista)
