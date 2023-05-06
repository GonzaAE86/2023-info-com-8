from datetime import date

fecha_nacimiento = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")
dia, mes, anio = fecha_nacimiento.split('/')
edad = date.today().year - int(anio) - ((date.today().month, date.today().day) < (int(mes), int(dia)))
print("Su edad es:", edad, "años.")
