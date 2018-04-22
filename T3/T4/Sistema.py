from Usuario import Usuario
from Guest import Guest
from Regular import Regular
from Group import Group
from Root import Root

def Sistema():
    u = Usuario("Eduardo")	
    u.boasVindas()
		
    g1 = Guest("Caio")
    g1.boasVindas()
    g1.descreveGuest()
    g1.despedidaGuest()
		
    r1 = Regular("Felipe")
    r1.boasVindas()
    r1.dashboard()
    r1.descreveRegular()
    r1.despedidaRegular()
		
    g2 = Group("Grupo Python")
    g2.boasVindas()
    g2.descreveGroup()
    g2.groupBoard()
    g2.despedidaGroup()
		
    r2 = Root("root")
    r2.boasVindas()
    r2.descreveRoot()
    r2.excluirTodos()
    r2.despedidaRoot()
	
Sistema()