"""Exemplo de herança"""

print("Exemplo de herança")


class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")
        return

    def emitir_som(self):
        pass


class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"


class Gato(Animal):
    def emitir_som(self):
        return "Miau"


dog = Cachorro("Lineu")
cat = Gato("Bills")


"""Exemplo de polimorfismo"""

print("\nExemplo de polimorfismo")

animais = [dog, cat]

for animal in animais:
    print(f"O {animal.nome} faz: {animal.emitir_som()}")


"""Exemplo de encapsulamento"""

print("\nExemplo de encapsulamento")


class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo

    def depositar(self, valor):
        self.valor = valor

        if self.valor > 0:
            self.__saldo += self.valor

    def sacar(self, valor):
        self.valor = valor

        if self.valor > 0 and self.valor <= self.__saldo:
            self.__saldo -= self.valor

    def consultar_saldo(self):
        return self.__saldo


conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta.depositar(valor=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta.depositar(valor=-1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta.sacar(valor=1383)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")


"""Exemplo de abstração"""

print("\nExemplo de abstração")

from abc import ABC, abstractmethod


class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro ligado usando a chave"

    def desligar(self):
        return "Carro desligado usando a chave"


carro_amarelo = Carro()

print(carro_amarelo.ligar())
print(carro_amarelo.desligar())
