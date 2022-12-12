escolha = input("Escolha, Digite '1' para a função 1 e '2' para a função 2: ")
if escolha == "1":
    def func1(x): #cabeçalho da função func1 com o parâmetro formal x.
        return x+1
    s = func1(10) #aqui a função func1 é chamada com o parâmetro real 10.
else:
    def func2(x):
        return x +2
    s = func2(10)
print(s)