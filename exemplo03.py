inicial = int(input('Entre com o valor inicial: '))
final = int(input('Entre com o valor final: '))



def verificar_pares(valor_inicial, valor_final):
    contador = 0
    while valor_inicial <= valor_final:
        if valor_inicial % 2 == 0:
            contador += 1
        valor_inicial += 1

    return contador

resultado = verificar_pares(inicial, final)
print(resultado)