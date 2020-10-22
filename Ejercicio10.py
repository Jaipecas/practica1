ano = int(input("Introduzca un año: "))


def es_bisiesto(ano):
    if ano % 4 == 0:
        print(f"El año {ano} es bisiesto")
    elif ano % 100 != 0:
        print(f"El año {ano} no es bisiesto")

es_bisiesto(ano)