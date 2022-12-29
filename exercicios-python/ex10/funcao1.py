

valor = 20


def multiplica(fator):
    """Função não pura"""
    global valor
    valor = valor * fator
    print("Resultado: ", valor)


def main():
    numero = int(input("Digite o fator: "))
    multiplica(numero)
    multiplica(numero)


if __name__ == '__main__':
    main()
