# x = [i for i in range(0,10) if i%2==0]
# print(x)

class Pessoa():
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def __str__(self):
        print(f'{self.nome}\n{self.idade}\n{self.cpf}')



    @classmethod # Métodos ligados à classe em si, e não às instâncias de classe
    def definir_genero(cls, genero): # cls é um parâmetro que recebe o estado da classe - não é o mesmo que método estático
        cls.genero = genero


#======================================================================
# Métodos estáticos - método que pode ser chamado somente pela classe, sem necessidade de instâncias
# Se diferencia dos métodos de classe por ser apenas um método utilitário, ou seja, não consegue 
# acessar nem modificar nenhum atributo ou método de classe

    @staticmethod
    def maior_de_idade(idade):
        x = lambda: True if idade > 18 else False
        print(x())

p1 = Pessoa('Bruno Teixeira', 24, '130.615.596-71')
p1.__str__()

p1.maior_de_idade(23)

