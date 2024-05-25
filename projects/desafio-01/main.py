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

    def listar_contatos(self, lista_de_contatos):
        print("\nLista de contatos")
        print("-" * 45)
        for indice, contato in enumerate(lista_de_contatos, start=1):
            favorito = "⭐" if contato["favorito"] else " "
            nome_contato = contato["nome"]
            telefone_contato = contato["telefone"]
            email_contato = contato["email"]
            print(
                f"{indice}"
                f"\nFavorito: [{favorito}]"
                f"\nNome: {nome_contato}"
                f"\nTelefone: {telefone_contato}"
                f"\nEmail: {email_contato}"
            )
            print("-" * 45)
        return


lista_de_contatos = []

while True:
    print("\nMenu do gerenciador de lista contatos:")
    print("1. Adicionar um contato")
    print("2. Visualizar a lista de contatos cadastrados")
    print("3. Editar um contato")
    print("4. Marcar/desmarcar um contato como favorito")
    print("5. Ver uma lista de contatos favoritos")
    print("6. Apagar um contato")
    print("7. Sair")

    escolha = str(input("\nDigite a opção desejada: "))
    elif escolha == "7":
        print("Programa finalizado")
        break
        print("Opção Invalida")
