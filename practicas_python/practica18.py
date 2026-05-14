# Actividad 18: Función para calcular el precio con IVA
# Define una función que calcula el precio final incluido IVA (21%).

# Defino una función llamada 'calcular_precio_con_iva'
# Las funciones son bloques de código reutilizables que realizan una tarea específica
# El parámetro 'precio' es el valor que recibirá la función
def calcular_precio_con_iva(precio):
    # Defino el porcentaje de IVA (21% = 0.21)
    iva = 0.21
    
    # Calculo el precio final multiplicando el precio por (1 + iva)
    # Por ejemplo: precio=100, IVA=0.21 → 100 * 1.21 = 121
    precio_final = precio * (1 + iva)
    
    # return devuelve el resultado de la función al lugar donde fue llamada
    return precio_final

# Pido al usuario el precio del producto
precio_producto = float(input("Introduce el precio del producto informático: "))

# Llamo a la función con el precio introducido
# El resultado se guarda en la variable precio_final
precio_final = calcular_precio_con_iva(precio_producto)

# Muestro el precio sin IVA
print(f"Precio sin IVA: {precio_producto}€")

# Muestro el precio con IVA aplicado
print(f"Precio con IVA (21%): {precio_final}€")