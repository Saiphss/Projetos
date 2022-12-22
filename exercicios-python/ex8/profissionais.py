from pessoas import Pessoa

class Profissional(Pessoa):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self.profissao = profissao
    def imprimir(self):
        super().imprimir()
        '''Exemplo de polimorfismo'''
        print("\t e trabalha como ",self.profissao)

p1 = Profissional("Ana",31,"Dentista")
p1.imprimir()