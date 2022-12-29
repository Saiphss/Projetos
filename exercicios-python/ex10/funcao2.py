valor = 20


def multiplica(valor, fator):
    """A função multiplica deste script é um exemplo de funçaõ pura"""
    valor = valor * fator
    return valor


def main():
    
    numero = int(input("Digite o fator: "))
    print("Resultado: ",multiplica(valor, numero))
    print("Resultado: ",multiplica(valor, numero))


if __name__ == '__main__':
    main()