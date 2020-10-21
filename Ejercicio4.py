cadena = input("Introduzca una palabra: ")
totalMayus = 0

for caracter in cadena:
    if caracter.isupper():
        totalMayus += 1

print(f"El número de letras mayúsculas presentes en la palabra introducida son: {totalMayus}")
