#Após ler mais, atualizar se necessário.
x = eval(input("Função multiplica, digite um número: "))
y = eval(input("Função multiplica, digite mais um número: "))
if x or y > 0:
    def multiplique(x,y):
        valor_result = x*y
        return valor_result
    resultMult = multiplique(x,y)
    print(f"O resultado é: {resultMult}")
else:
    print("Porfavor, digite apenas números válidos!")