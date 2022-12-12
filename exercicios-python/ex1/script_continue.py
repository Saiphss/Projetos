#Instrução auxiliar Continue
"""Atua sobre repetições dos laços for e while, porém, diferentemente da instrução break que interrompe todas as repetições do laço, a instrução auxiliar 'continue' interrompe apenas a iteração corrente, fazendo com que o laço passe para a próxima iteração.
"""
for num in range(1,11):
    if num == 5:
        continue
    else:
        print(num)
print("Laço encerrado.")

#Alterando a instrução auxiliar continue pela instrução break o laço encerraria quando o valor de num fosse igual a 5.