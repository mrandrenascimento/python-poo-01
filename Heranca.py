from abc import ABC, abstractmethod
import os
os.system ("cls||clear")

class Funcionario(ABC):
    def __init__(self,nome:str, idade:int, salario:float) -> None:
        self.nome=nome
        self.idade=idade
        self.salario=salario
    
    @abstractmethod
    def calcular_salario(self)->float :
        pass

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        BONIFICACAO = 1.2 #ACRESCIMO DE 20%, e desconto 0.2 desconto de 20%
        salario_Final = self.salario*BONIFICACAO
        return salario_Final

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh:str) -> None:
        super().__init__(nome, idade, salario)    
        self.cnh= cnh
    def calcular_salario(self) -> float:
        BONIFICACAO = 1.1 #ACRESCIMO DE 20%, e desconto 0.2 desconto de 20%
        salario_Final = self.salario*BONIFICACAO
        return salario_Final

#Instanciar classes 
#funcionario1=Funcionario("José",33,1000.00)
#print(f"Nome: {funcionario1.nome}")

gerente1 = Gerente("José",23,1000.00)
print(f"Nome: ",gerente1.nome)
print(f"Salário: ",gerente1.calcular_salario())

motoboy1 = Motoboy("Maria",35,1000.00,"n656568")
print(f"\nNome: ",motoboy1.nome)
print(f"CNH: ",motoboy1.cnh)
print(f"Salário: ",motoboy1.calcular_salario())