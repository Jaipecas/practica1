ano = int(input("Introduza el año en curso: "))
lista = []

for i in range(3):
    nombre = input("Introduzca su nombre: ")
    anoNacimiento = input("Introduzca año de nacimiento: ")
    lista.extend([nombre, anoNacimiento])

indiceNombre = 0
indiceAños = 1

while indiceNombre < len(lista):
    nombre = lista[indiceNombre]
    anoNac = int(lista[indiceAños])
    edad = ano - anoNac
    print(f"{nombre} tiene {edad} años")
    indiceAños += 2
    indiceNombre += 2
