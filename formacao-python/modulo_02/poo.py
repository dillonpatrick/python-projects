class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."


pessoa1 = Pessoa("Dillon", 29)
pessoa2 = Pessoa("Patrick", 30)

print(pessoa1.saudacao())

print(pessoa2.saudacao())
