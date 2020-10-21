edadesLista = []
edadesTupla = ()
for i in range(10):
    edad = int(input("Introducir edad: "))
    edadesLista.append(edad)

edadesTupla = tuple(edadesLista)

cantidad = 0
for edad in edadesTupla:
    if edad > 20:
        cantidad +=1

print(f"La cantidad de personas con edades superiores a 20 años es: {cantidad}")

