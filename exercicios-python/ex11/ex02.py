# Higher order function


def multiplicar_por(multiplicador):
    def multi(multiplicando):
        return multiplicando * multiplicador
    return multi

def main():
    """ o multiplicando da função multi será multiplicado por 10, ou seja, o parâmetro da função multiplica_por está
    recebendo o valor 10 """
    multiplicar_por_10 = multiplicar_por(10)
    """ definindo o valor do multiplicando (parâmetro da função multi) """
    """ Resultado: 10 """
    print("Resultado: ", multiplicar_por_10(1))
    """ Resultado: 20 """
    print("Resultado: ", multiplicar_por_10(2))

    multiplicar_por_5 = multiplicar_por(5)
    """ Resultado: 5 """
    print("Resultado: ", multiplicar_por_5(1))
    """ Resultado: 10 """
    print("Resultado: ", multiplicar_por_5(2))


if __name__ == '__main__':
    main()