class Contatos:
    def __init__(self, nome=" ", telefone=" ", email=" ", favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

    def adicionar_contato(self, lista_de_contatos):
        contato = {
            "nome": self.nome,
            "telefone": self.telefone,
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
            favorito = "✔" if contato["favorito"] else " "
            nome_contato = contato["nome"]
            telefone_contato = contato["telefone"]
            email_contato = contato["email"]
            print(
                f"Indice: {indice}"
                f"\nFavorito: [{favorito}]"
                f"\nNome: {nome_contato}"
                f"\nTelefone: {telefone_contato}"
                f"\nEmail: {email_contato}"
            )
            print("-" * 45)

        return

    def editar_contato(self, lista_de_contatos, indice_contato, chave, novo_valor):
        indice = int(indice_contato) - 1

        if indice >= 0 and indice < len(lista_de_contatos):
            if chave == "nome" or chave == "telefone" or chave == "email":
                lista_de_contatos[indice].update({chave: novo_valor})
                print(f"O contato foi atualizado(a).")
            else:
                print("Campo inválido.")
        else:
            print("Indice inválido")

        return

    def favorita_contato(self, lista_de_contatos, indice_contato):
        indice = int(indice_contato) - 1

        if indice >= 0 and indice < len(lista_de_contatos):
            if lista_de_contatos[indice]["favorito"]:
                lista_de_contatos[indice].update({"favorito": False})
                print(f"O contato foi atualizado(a).")
            else:
                lista_de_contatos[indice].update({"favorito": True})
                print(f"O contato foi atualizado(a).")
        else:
            print("Indice inválido")

        return self.listar_contatos(lista_de_contatos)

    def listar_favoritos(self, lista_de_contatos):
        print("\nLista de contatos favoritos")
        print("-" * 45)

        if len(lista_de_contatos):
            for indice, contato in enumerate(lista_de_contatos, start=1):
                favorito = "✔" if contato["favorito"] else " "
                if contato["favorito"]:
                    print(
                        f"Indice: {indice}"
                        f"\nFavorito: [{favorito}]"
                        f"\nNome: {contato['nome']}"
                        f"\nTelefone: {contato['telefone']}"
                        f"\nEmail: {contato['email']}"
                    )
                print("-" * 45)
        else:
            print("Lista vazia.")

        return

    def deletar_contato(self, lista_de_contatos, indice_contato):
        indice = int(indice_contato) - 1

        if indice >= 0 and indice < len(lista_de_contatos):
            del lista_de_contatos[indice]
            print(f"Contato deletado")
        else:
            print("Indice inválido")

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

    if escolha == "1":
        nome_contato = input("Digite o nome do contato: ")
        if nome_contato:
            telefone_contato = input("(Opcional) Digite o telefone do contato: ")
            email_contato = input("(Opcional) Digite o email do contato: ")

            Contatos(nome_contato, telefone_contato, email_contato).adicionar_contato(
                lista_de_contatos
            )
        else:
            print("O nome do contato é obrigatório.")

    elif escolha == "2":
        Contatos().listar_contatos(lista_de_contatos)

    elif escolha == "3":
        Contatos().listar_contatos(lista_de_contatos)
        indice_contato = input("Digite o indice do contato a ser editado: ")
        chave = (
            input("Qual campo deseja atualizar (nome, email, telefone): ")
            .lower()
            .strip()
        )

        novo_valor = input("Digite o valor atualizado: ")

        Contatos(nome_contato, telefone_contato, email_contato).editar_contato(
            lista_de_contatos, indice_contato, chave, novo_valor
        )

    elif escolha == "4":
        Contatos().listar_contatos(lista_de_contatos)
        indice_contato = indice_contato = input(
            "Digite o indice do contato que deseja marcar/desmarcar como favorito: "
        )
        Contatos().favorita_contato(lista_de_contatos, indice_contato)

    elif escolha == "5":
        Contatos().listar_favoritos(lista_de_contatos)

    elif escolha == "6":
        Contatos().listar_contatos(lista_de_contatos)
        indice_contato = input("Digite o indice do contato que deseja remover: ")
        Contatos().deletar_contato(lista_de_contatos, indice_contato)

    elif escolha == "7":
        print("Programa finalizado")
        break
    else:
        print("Opção Inválida")
