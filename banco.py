class ContaBancaria:
    def __init__(self, dono):
        self.dono = dono
        self.__saldo = 0  # aqui
        
    def depositar(self, valor):
        self.__saldo = self.__saldo + valor  # aqui
        
    def sacar(self, valor):
        if valor > self.__saldo:  # aqui
            print("Saldo insuficiente!")
        else:
            self.__saldo = self.__saldo - valor  # aqui
    
    def ver_saldo(self):
        return self.__saldo  # aqui
        
    def extrato(self):
        print("Titular:", self.dono)
        print("Saldo:", self.__saldo)  # aqui
            
                      
            
    
conta_maria = ContaBancaria("Maria")
print("Saldo da conta:", conta_maria.ver_saldo());
conta_maria.depositar(500)
print("Deposito em conta:", conta_maria.ver_saldo());
conta_maria.sacar(200)
conta_maria.ver_saldo()
print("Saldo atual da conta:", conta_maria.ver_saldo())
print("\nExtrato:")
conta_maria.extrato()
   
conta_joao = ContaBancaria("Joao")
print("\nSaldo da conta:", conta_joao.ver_saldo());
conta_joao.depositar(1000)
print("Deposito em conta:", conta_joao.ver_saldo());
conta_joao.sacar(700)
print("Saldo atual da conta:", conta_joao.ver_saldo())
print("\nExtrato:")
conta_joao.extrato()

class ContaPoupanca(ContaBancaria):
    # aqui vai o que é diferente da conta normal
    def render_juros(self):
        juros = self.ver_saldo() * 0.01
        self.depositar(juros)

conta_ana = ContaPoupanca("Ana")
print("\nSaldo da conta:", conta_ana.ver_saldo());
conta_ana.depositar(1000)
print("Deposito em conta:", conta_ana.ver_saldo());
conta_ana.render_juros()
print("Rendimento da conta: ", conta_ana.ver_saldo());

print("\nExtrato:")
conta_ana.extrato()    

class ContaCorrente(ContaBancaria):
    
    def sacar(self, valor):
        if valor > self.ver_saldo() + 500:
            print("Saldo insuficiente!")
        else:
            self.depositar(-valor)
            
conta_julia = ContaCorrente("Julia")
conta_julia.depositar(200)
print("\nSaldo da conta:", conta_julia.ver_saldo());
conta_julia.sacar(600)
conta_julia.ver_saldo()
conta_julia.sacar(800)
print("Apos saque de 800:", conta_julia.ver_saldo())

print("\nExtrato:")
conta_julia.extrato() 