import os
from enum import Enum
class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Pessoa:    
    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        """Contrutor."""
        self.nome=nome
        self.idade=idade
        self.sexo = sexo
    
    def __str__(self) -> str:
        """Equivale ao toString() do java."""
        return(f"\nNome: {self.nome}"
               f"\nIdade: {self.idade}"
               f"\nSexo: {self.sexo.value}"
               )
    
#Instanciando Classe Pessoa.
os.system("cls||clear")

pessoa_p1 = Pessoa("Marta",22,Sexo.FEMININO)
print(pessoa_p1)