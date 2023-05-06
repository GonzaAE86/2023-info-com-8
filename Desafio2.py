# Solicita la información personal del usuario
nombre_completo = input("Ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura en cm: "))
peso = float(input("Ingrese su peso en kg: "))
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su número de teléfono: ")

# Imprime la información ingresada por el usuario en el formato especificado
print("La información ingresada es la siguiente:")
print("Nombre completo: {}".format(nombre_completo))
print("Edad: {}".format(edad))
print("Estatura: {} cm".format(estatura))
print("Peso: {} kg".format(peso))
print("Dirección: {}".format(direccion))
print("Número de teléfono: {}".format(telefono))