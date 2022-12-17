escolha = eval(input("Para multiplicar digite 1, para somar digite 2: "))
if escolha == 1:
    def mult(x,y):
        result = x*y
        return result
    n1 = eval(input("Digite um número para multiplicar: "))
    n2 = eval(input("Digite mais um número para multiplicar: "))
    print(f"Resultado da multiplicação: {mult(n1,n2)}")
elif escolha == 2:
    def soma(x, y):
        resultSoma = x + y
        return resultSoma
    n1 = eval(input("Digite um número para somar: "))
    n2 = eval(input("Digite mais um número para somar: "))
    print(f"Resultado da soma: {soma(n1, n2)}")
else:
    print("Digite apenas números válidos!")
