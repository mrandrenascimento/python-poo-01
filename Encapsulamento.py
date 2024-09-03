import os
os.system("cls||clear")
# Criando sua propria excessão
class SaldoInsuficienteError(Exception):
    pass

class ValorNegativoError(Exception):
    pass

class Conta:
    def __init__(self,numero_conta:int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia=agencia
        self._saldo = 0 # Atributo protegido
    
    @property
    def saldo(self):
        return self._saldo

    def sacar(self,valor)-> float:
        #try - except
        try:
            self.__verificar_saque(valor)

        except SaldoInsuficienteError as error:
            return f"Erro: {error}"
         
        self._saldo -= valor
        return self._saldo
    
    def __verificar_saque(self,valor): # Método Privado.
            if valor>self.saldo:
                raise SaldoInsuficienteError("Saldo Insuficiente.") # Lançando um Erro
   
    
    def depositar(self,valor)->float:
        
        try :
            self.__verificar_deposito(valor)

        except ValorNegativoError as erro:
            return f"Erro: {erro}"
    
        self._saldo += valor
        return self._saldo
    
    def __verificar_deposito(self,valor):
        if valor<0:
            raise ValorNegativoError("Não é Possivel Depositar Valor Negativo")        
class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

#Instanciar as Classes
conta_corrente=ContaCorrente(222,333)
conta_poupanca=ContaPoupanca(444,555)

print(conta_corrente.saldo)

print(conta_corrente.depositar(-200))

print(conta_corrente.saldo)