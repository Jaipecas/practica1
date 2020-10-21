listaNombres = ["jaime", "alberto", "juan", "antonio", "pepe"]
letra = input("Introduzca la letra a buscar: ")
listaNombresLetra = []
for nombre in listaNombres:
    if nombre[0] == letra:
        listaNombresLetra.append(nombre)

print(f"Los nombres que empiezan con la laetra {letra} son: {listaNombresLetra}")

