import os
os.system("cls||clear")
class Livro:
    def __init__(self,titulo:str, autor:str, numeroPaginas:int,preco:float) -> None:
        self.titulo=titulo
        self.autor=autor
        self.numeroPaginas=numeroPaginas
        self.preco=preco

    def exibir_Dados(self)->str:
        return f"Titulo: {self.titulo} \nAutor: {self.autor}\nNúmeros de Página: {self.numeroPaginas}\nPreço: {self.preco}"

#Instanciando a Classe.
   
livro = Livro("O Autor","O Livro",350, 351.50)
segundo_livro = Livro("O Livro","Autor",554, 510.50)

print(livro.exibir_Dados())
print(segundo_livro.exibir_Dados())
