def calcular_pares():
    numero = 100
    quantidade = 0

    while numero <= 200:
        if numero % 2 == 0:
            quantidade += 1
        quantidade += 1

    print(quantidade)

calcular_pares()