#Instrução auxiliar Break
"""A Instrução auxiliar Break interrompe as repetições dos laços for e while, ou seja, ao encontrar uma instrução break a execução do looping será interrompida.
"""
while True:
    palavra = input("Digite 'Sair' para encerrar o laço: ")
    if palavra == 'Sair':
        break
print("Comando aceito, o looping foi encerrado.")
