numero = int(input('Digite um número inteiro positivo: '))
fatorial = 1

while numero > 0:
    fatorial = fatorial * numero
    numero -= 1

print('Ofatorial desse número é: ', fatorial)
