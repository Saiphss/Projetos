from typing import Any


def calculaDelta(coeficiente1, coeficiente2, coeficiente3):
    #Delta da eq 2º grau = b^2 - 4.a.c
    delta = coeficiente2*coeficiente2 - 4*coeficiente1*coeficiente3
    return delta
a = eval(input("Entre com o coeficiente a da equação: "))
b = eval(input("Entre com o coeficiente b da equação: "))
c = eval(input("Entre com o coeficiente c da equação: "))

delta = calculaDelta(a, b, c)

print(f'O valor calculado foi {delta}')

#Delta > 0 a equação tem 2 raizes reais
#Delta ==0 a equação tem 1 raiz real
#Delta <0 a equação não tem raiz real

if delta > 0:
    print("A equação tem 2 raizes reais")
elif delta == 0:
    print("Equção tem 1 raiz real")
else:
    print("A equaçaõ não tem raiz real")
