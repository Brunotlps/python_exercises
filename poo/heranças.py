class PessoaComum:
    def falar(self):
        print("Olá")
    
    def trabalhando(self):
        print("Trabalhando")

class Pessoa1(PessoaComum):
    @classmethod
    def definir_profissao(cls, profissao):
        cls.profissao = profissao
        
dev = Pessoa1()
dev.definir_profissao('Engenheiro de Software')
print(dev.profissao)
dev.falar()