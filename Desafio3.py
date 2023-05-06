texto = input("Ingrese un texto: ")
letra1 = input("Ingrese la primera letra a buscar: ").lower()
letra2 = input("Ingrese la segunda letra a buscar: ").lower()
letra3 = input("Ingrese la tercera letra a buscar: ").lower()

# 1- Cantidad de veces que aparece cada una de las letras
letras = [letra1, letra2, letra3]
contador = {}
for letra in letras:
    contador[letra] = texto.lower().count(letra)

print("Cantidad de veces que aparecen las letras:")
for letra, cantidad in contador.items():
    print(f"{letra}: {cantidad}")

# 2- Cuántas palabras hay en total en todo el texto
palabras = texto.split()
cantidad_palabras = len(palabras)
print(f"Cantidad de palabras: {cantidad_palabras}")

# 3- Primera y última letra
primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"Primera letra: {primera_letra}")
print(f"Última letra: {ultima_letra}")

# 4- Texto en orden inverso
texto_inverso = texto[::-1]
print(f"Texto en orden inverso: {texto_inverso}")

# 5- Si la palabra "python" aparece en el texto
contiene_python = "python" in texto.lower()
mensaje_contiene_python = {True: "El texto contiene la palabra 'python'", False: "El texto no contiene la palabra 'python'"}
print(mensaje_contiene_python[contiene_python])
