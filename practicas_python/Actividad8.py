lista_alumnos = []

for numero in range (1,6):
    print(f"introduce los datos del alumno {numero}")
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    persona = { 
        "nombre": {nombre},
        "apellido": {apellido}
    }
    lista_alumnos.append(persona)

for alumno in lista_alumnos:
    print(alumno["nombre"])
    print(alumno["apellido"])