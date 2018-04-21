from Doc import Doc
from Cliente import Cliente

def banco():
    c1 = Cliente("Eduardo", 1200.00, 5000.00)
    c2 = Cliente("Carlos", 2000.00, 900.00)

    print("Telas saques: ")
    c1.Sacar(6200.00)
    print("Saldo do cliente: ", c1.getNome()," é: ",c1.checarSaldo())
    c2.Sacar(100.0)
    print("Saldo do cliente, ", c2.getNome()," é: ", c2.checarSaldo())
    c2.Sacar(3000.0)	
	
    d1 = Doc()
		
    print("------------------------ Tela Docs: -------------------------------")
    print("Saldo inicial do cliente, ", c1.getNome(),", é: ", c1.checarSaldo())
    print("Saldo inicial do cliente, ", c2.getNome(),", é: ", c2.checarSaldo())
    print("------------------------ Transferência 1: --------------------------")
    d1.transferir(c1, c2, 300.00)
    print("Saldo atualizado do cliente, ", c1.getNome(),", é: ", c1.checarSaldo())
    print("Saldo atualizado do cliente, ", c2.getNome(),", é: ", c2.checarSaldo())
    print("------------------------ Transferência 2: --------------------------")
    d1.transferir(c1, c2, 30000.00)
    print("Saldo atualizado do cliente, ", c1.getNome(),", é: ", c1.checarSaldo())
    print("Saldo atualizado do cliente, ", c2.getNome(),", é: ", c2.checarSaldo())
    print("------------------------ Transferência 3: --------------------------")
    d1.transferir(c1, c2, 5900.00)
    print("Saldo atualizado do cliente, ", c1.getNome(),", é: ", c1.checarSaldo())
    print("Saldo atualizado do cliente, ", c2.getNome(),", é: ", c2.checarSaldo())
banco()