class Lamp:    

    def _init_(self,click,contador,qtdClicks):
        self.qtdClicks = qtdClicks
        self.click = click
        self.contador = contador


    def checarClick (self):
        if(self.click==False):
            print('A luz está desligada!')
        else:
            print('A luz está ligada')

    def clicar (self):        
        if (self.contador>=self.qtdClicks):
            print("A lâmpada está queimada")
            self.click=False
        elif (self.click==True):
            self.click=False
        else:
            self.click=True
        
        self.contador+=1