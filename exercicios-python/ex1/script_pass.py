##Instrução auxiliar Pass
"""Atua sobre a estrutura 'if' e permite que ela seja escrita sem outras intruções a serem executadas caso a condição seja verdadeira."""
for num in range(1, 10):
    if num % 2 == 0:
        pass
    else:
        print(num)
print('Laço encerrado')