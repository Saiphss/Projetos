nome = str(input('Digite seu nome: '))
numero = eval(input('Digite um número inteiro: '))

if numero%2 == 0:
    print(f'Olá {nome}, numero informado é par.')
else:
    print(f'Olá {nome}, o número informado é impar.')
