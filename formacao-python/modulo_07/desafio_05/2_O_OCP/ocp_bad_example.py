"""
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

"""

from abc import ABC, abstractmethod


class AprovaExame(ABC):
    @abstractmethod
    def aprovar_solicitacao_exame(self, exame):
        pass

    @abstractmethod
    def verifica_condicoes_do_exame(self, exame):
        pass


class AprovaExameSangue(AprovaExame):
    def aprovar_solicitacao_exame(self, exame):
        if self.verifica_condicoes_do_exame(exame):
            print(f"Exame {exame} aprovado!")

    def verifica_condicoes_do_exame(self, exame):
        return exame


class AprovaExameRaioX(AprovaExame):
    def aprovar_solicitacao_exame(self, exame):
        if self.verifica_condicoes_do_exame(exame):
            print(f"Exame de {exame} aprovado!")

    def verifica_condicoes_do_exame(self, exame):
        return exame


# Exemplo de uso:
class Exame:
    def __init__(self, tipo: str) -> str:
        self.tipo = tipo


exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

aprovador_exame_sangue = AprovaExameSangue()
aprovador_raiox = AprovaExameRaioX()

aprovador_raiox.aprovar_solicitacao_exame(exame_raio_x.tipo)
aprovador_exame_sangue.aprovar_solicitacao_exame(exame_sangue.tipo)
