import os
from enum import Enum
class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    RECURSOS_HUMAMNOS = "Recursos Humanos"
    MARKETING = "Marketing"

class Funcionario:    
    def __init__(self,id:int, nome:str, idade:int, salario:float, ) -> None:
        pass
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