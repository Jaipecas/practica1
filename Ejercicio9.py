palabra = input("Introduzca una palabra: ")


def contar_vocales(palabra):
    contadorA = 0
    contadorB = 0
    for letra in palabra:
        if letra == "a":
            contadorA += 1
        if letra == "e":
            contadorB += 1

    print(f"La palabra introducida tiene {contadorA} 'a' y {contadorB} 'e'")

contar_vocales(palabra)