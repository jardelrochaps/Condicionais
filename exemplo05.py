from random import randint

num = int(input('Digite um número entre 1 e 10: '))
soma = 0
nomero_sorteao = randint(1,10)
print('sorteou: ', numero_sorteado)

while num != numero_sorteado:
    soma = soma + numero_sorteado
    numero_sorteado = randint(1,10)
    print('Sorteou: ', numero_sorteado)

print('A soma é: ', soma)