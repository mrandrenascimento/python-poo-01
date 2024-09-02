import os
os. system ("cls||clear")
class Endereco:
    def __init__(self, logradouro:str, numero:int) -> None:
        self.logradouro = logradouro
        self.numero = numero
    def __str__(self)->str:
        return f"Logradouro: {self.logradouro}\nNúmero: {self.numero}"

class Aluno:
    def __init__(self,nome:str,idade:int,endereco:Endereco) -> None:
        #Atributos
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    def __str__(self)->str:
        return  f"Nome: {self.nome} \nIdade: {self.idade}\nEndereço:{self.endereco}" 


#instanciando a Classe 
aluno = Aluno("Marta",22,Endereco("Travessa Orlando", 45))

print(aluno)
