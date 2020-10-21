ano = int(input("Introduza el año en curso: "))
diccionario = {}

for i in range(3):
    nombre = input("Introduzca su nombre: ")
    anoNacimiento = int(input("Introduzca año de nacimiento: "))
    diccionario[nombre] = anoNacimiento

for nombre, anoNac in diccionario.items():
    edad = ano - anoNac
    print(f"{nombre} tiene {edad} años")

