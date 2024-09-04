class Pessoa():
    def falar(self):
        print("Olá")
    
    def trabalhando(self):
        print("Trabalhando")

class Profissional(Pessoa):
    @classmethod
    def definir_profissao(cls, profissao):
        cls.profissao = profissao
    
    def falar(self): # Esse método tem prioridade sobre o método da classe pai
        # super().falar() referencia o método da classe pai diretamente
        print("Eae") 