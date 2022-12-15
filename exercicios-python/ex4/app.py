#Captura e manipulação de exceções
#Instruções try/except

try:
    num = eval(input("Digite um número: "))
    print(num)
except:
    print("Apenas valores númericos são permitidos!")
