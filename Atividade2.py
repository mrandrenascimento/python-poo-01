from abc import ABC, abstractmethod
import os

os. system("cls||clear")

class Endereco:
    def __init__(self, logradouro: str, numero:str, cidade:str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}"
                f"\nNúmero: {self.numero}"
                f"\nCidade: {self.cidade}"
                )    

class Funcionario(ABC):
    def __init__(self, nome:str, email:str, salario:str, endereco:Endereco) -> None:
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco

    @abstractmethod
    def salario_Final(self)->float:
        pass
    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nE-mail: {self.email}"
                f"\nSalário: {self.salario}"
                f"\nEndereço: {self.endereco}"
                )    
class Motoboy(Funcionario):
    def __init__(self, nome: str, email: str, cnh:str, salario: str, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)    
        self.cnh = cnh 
    def salario_Final(self) -> float:
        return 1000.00
    
Motoboy motoboy = Motoboy()