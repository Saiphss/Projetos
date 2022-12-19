class Cachorro:
    def __init__(self, nome):
        self.nome = nome
        print(f"{self.nome} é um nome muito bonito!")

nome_dog = input("Digite o nome do seu cachorro: ")
c1 = Cachorro(nome_dog)