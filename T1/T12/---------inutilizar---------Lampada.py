class Lampada:    
	def __ini__(self, estado, limite):
		self.estado = estado
    	self.limite = limite
    	self.count = 0

    def turnOn(self):
        if(self.count >= self.limite):
	        print("Impossível prosseguir, lâmpada está queimada")
	        self.estado = False
        else:
	        self.estado = True
	self.count = count + 1

    def turnOff(self):
        if(self.count >= self.limite):
            print("Impossível prosseguir, lâmpada está queimada")
            self.estado = False
	    else:
		    print("Ligada")
	self.estado = True
	self.count = count + 1

    def setLimite(self, l):
	    self.limite = l

    def getLimite(self):
	    return self.limite

    def status(self):
	    if(self.estado==self.true):
		    print("Lâmpada está ligada")
	    else:
		    print("Lâmpada está desligada")
