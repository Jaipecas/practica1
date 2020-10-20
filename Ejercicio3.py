listaPalabras = ["lunes", "martes", "miércoles", "jueves", "viernes"]
numCaracteres = int (input("Introduzca el número mínimo de caracteres que quiere que tengan las palabras de la lista: "))

def filtrar_palabras(lista, entero):
    listaPalabras = []
    for palabra in lista:
        if len(palabra) >= entero:
            listaPalabras.append(palabra)
    return listaPalabras

listaFiltrada = filtrar_palabras(listaPalabras, numCaracteres)
print(f"Las palabras de la lista que tienen {numCaracteres} o más caracteres son: {listaFiltrada}")
