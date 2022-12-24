import datetime
from extratos import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.dataAbertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(
            ["DEPOSITO", valor, "DATA", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["SAQUE", valor, "DATA", datetime.datetime.today()])
            return True

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ("Saldo insuficiente para realizar esta operação!")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            return "Transferencia Realizada"
