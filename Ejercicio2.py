listaPalabras = ["lunes", "martes", "miércoles", "jueves", "viernes"]


def mas_larga(lista):
    palabraMax = ""
    for palabra in lista:
        if len(palabra) > len(palabraMax):
            palabraMax = palabra
    return palabraMax

palabraMax = mas_larga(listaPalabras)
print(f"La palabra más larga de la lista es: {palabraMax}")
