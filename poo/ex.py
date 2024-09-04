# class Carro:
#     ano_atual = 2024
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
    
#     def informacoes(self):
#         return f'marca : {self.marca}\nmodelo: {self.modelo}\nano: {self.ano}'
    
#     def idade(self):
#         return f'{self.ano_atual - self.ano}'


# carro1 = Carro('Fiat', 'Palio', 2010)
# print(carro1.informacoes())
# print(carro1.idade())

# ==========================================================================================================================

# class ContaBancaria():
#     taxa_juros = 0.05
    
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
    
#     def depositar(self, valor_deposito):
#         self.saldo += valor_deposito
#         print(f'Depósito efetuado com sucesso.\nValor depósito = {valor_deposito}R$\nSaldo atual = {self.saldo}R$')


# c1 = ContaBancaria('Bruno', 1000)

# c1.depositar(100)

# =================================================================================================================================

class BombaCombustivel: 
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
        print(f"tipo do combustível: {tipo_combustivel}\nvalor do litro: {valor_litro}R$\nquantidade: {quantidade_combustivel:.2f}l")


    def abastecer_valor(self, valor_solicitado):
        quantidade_abastecida = valor_solicitado / self.valor_litro
        self.quantidade_combustivel -= quantidade_abastecida
        print(f"Quantidade abastecida: {quantidade_abastecida:.2f}\nQuantidade restante de gasolina: {self.quantidade_combustivel:.2f}")

    
    def abastecer_por_litro(self, quantidade_litros):
        quantidade_abastecida = quantidade_litros * self.valor_litro
        self.quantidade_combustivel =- quantidade_abastecida
        valor = quantidade_litros * self.valor_litro
        print(f"Valor: {valor:.2f}\n")



    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
        print(f"Valor do litro alterado: {self.valor_litro}R$")

b1 = BombaCombustivel('gasolina', 5.60, 100)
b1.abastecer_valor(100)
b1.abastecer_por_litro(45)
b1.alterar_valor(5.50)