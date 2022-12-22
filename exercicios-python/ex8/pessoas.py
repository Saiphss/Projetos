class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def imprimir(self):
        print(self.nome," tem",self.idade, "anos de idade" )
    def getIdade(self):
        return self.idade
    def setIdade(self):
        return self.idade

p1 = Pessoa("Ana",31)
p1.imprimir()