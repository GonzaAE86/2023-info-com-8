# Pedimos al usuario que ingrese su nombre y ventas del mes
nombre = input("Por favor, ingrese su nombre: ")
ventas = float(input("Ingrese sus ventas del mes: "))

# Calculamos la comisión del 6% sobre las ventas
comision = ventas * 0.06

# Mostramos al vendedor el monto que le corresponde por comisiones
print("¡Hola", nombre, "!, has vendido", ventas, "y tu comisión es de", comision, "pesos.")