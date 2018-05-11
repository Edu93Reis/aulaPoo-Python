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
    g1.descreve()
    g1.despedida()
		
    r1 = Regular("Felipe")
    r1.boasVindas()
    r1.dashboard()
    r1.descreve()
    r1.despedida()
		
    g2 = Group("Grupo Python")
    g2.boasVindas()
    g2.descreve()
    g2.groupBoard()
    g2.despedida()
		
    r2 = Root("root")
    r2.boasVindas()
    r2.descreve()
    r2.excluirTodos()
    r2.despedida()
	
Sistema()