listaNumeros = [3, 4, 1, 7, 9, 3, 1]


def max_in_list():
    num_max = 0
    for num in listaNumeros:
        if num > num_max:
            num_max = num
    return num_max


num = max_in_list()

print(f"El número mayor de la lista es: {num}")
