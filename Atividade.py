from abc import ABC, abstractmethod
import os
os.system ("cls||clear")

class Endereco:
    def __init__(self, logradouro:str, numero:str, complemento:str, cep:str, cidade:str) -> None:
        self.logradouro = logradouro
        self.numeto = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
    
    def __str__(self) -> str:
        return f"Logradouro: {self.logradouro}\nNúmero: {self.numeto}\nComplemento: {self.complemento}\nCep{self.cep}"    

class Funcionario(ABC):
    def __init__(self,nome:str, telefone:str, email:str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def salario_Final(self)->str :
        pass
   
    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\E-mail: {self.email}"
                f"\nSalário: {self.salario_Final()}"
                f"\nEndereço: {self.endereco}"
                )

class Engenheiro (Funcionario):
    def __init__(self, nome: str, telefone: str, crea:str, email: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)    
        self.crea= crea

    def salario_Final(self) -> str:
        return 2000.00


class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, crm:str, email: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)    
        self.crm=crm
    def salario_Final(self) -> str:
        return 5000.00

#Instanciar classes 

engenheiro_1 = Engenheiro("André","5633565","4545d","Andre@gmail.com",Endereco("Rua A","54","casa A","45166564","Salvador-Ba"))

print(f"Nome: {engenheiro_1.nome}")
print(f"Telefone: {engenheiro_1.telefone}")
print(f"E-mail: {engenheiro_1.email}")