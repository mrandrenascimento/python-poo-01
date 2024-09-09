import os
from enum import Enum
class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Finaceiro"
    RECURSOS_HUMAMNOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Funcionario:    
    def __init__(self,id:int, nome:str, idade:int, salario:float, setor:Setor, sexo:Sexo) -> None:
        self.id=id
        self.nome=nome
        self.idade=idade
        self.salario=salario
        self.setor = setor
        self.sexo=sexo

    def __str__(self) -> str:
        """Equivale ao toString() do java."""
        return(f"\nID: {self.id}"
               f"\nNome: {self.nome}"
               f"\nIdade: {self.idade}"
               f"\nSalário: {self.salario}"
               f"\nSetor: {self.setor.value}"
               f"\nSexo: {self.sexo.value}"
               )
    
#Instanciando Classe Funcionário.
os.system("cls||clear")

funcionario_1 = Funcionario(424,"João",23,1425.35,Setor.MARKETING, Sexo.MASCULINO)
print(funcionario_1)