cadena = input("Introduzca una palabra: ")
totalMayus = 0
i = 0

for caracter in cadena:
    if cadena[i].isupper():
        totalMayus += 1
    i += 1

print(f"El número de letras mayúsculas presentes en la palabra introducida son: {totalMayus}")
