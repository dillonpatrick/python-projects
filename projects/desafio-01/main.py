class Contatos:
    def __init__(self, nome=" ", telefone=" ", email=" ", favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

    def adicionar_contato(self, lista_de_contatos):
        contato = {
            "nome": self.nome,
            "telefone": self.telefone.replace(" ", ""),
            "email": self.email,
            "favorito": self.favorito,
        }

        lista_de_contatos.append(contato)
        print(f"O contato '{self.nome}' foi adicionado(a).")
        return
