
class Conta:
    def __init__(self,numero, titular, saldo, limite):
        print("Construindo Objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite



    def extrato(self):
        print("O saldo é {} do titular {}".format(self.__saldo, self.__titular))

    def numero_da_conta(self):
        print("O numero da conta do titular {} é {}".format(self.__titular, self.__numero))

    def depositar(self, valor):
        self.__saldo += valor

    def __saque_permitido(self, valor_saque):
        valor_disponível = self.__saldo + self.__limite
        return valor_saque <= valor_disponível

    def sacar(self,valor):
        if(self.__saque_permitido(valor)):
            self.__saldo -= valor
        else:
            print("Saque não autorizado")

    def transferir(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

