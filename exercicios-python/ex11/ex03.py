# Funções lambda


def multiplicar_por(multiplicador):
    return lambda multiplicando: multiplicando * multiplicador


def main():
    multiplicar_por_10 = multiplicar_por(10)
    print("Resultado: ", multiplicar_por_10(1))
    print("Resultado: ", multiplicar_por_10(2))

    multiplicar_por_5 = multiplicar_por(5)
    print("Resultado: ", multiplicar_por_5(1))
    print("Resultado: ", multiplicar_por_5(2))


if __name__ == '__main__':
    main()
