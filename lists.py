list_example = []

list_example.append("Bruno")
print(list_example)
print(len(list_example))

list_example.append("Alyne")
list_example.append("Carlos")

list_example.insert(0, "Ana")



print(list_example)

list_example.pop() #remove o último index
print(list_example)


list_example.pop(0)
print(list_example)


list_example.remove("Bruno")
print(list_example)

print(list_example.index("Alyne")) 

# list_example.pop.(list_example.index("Value")) - para remover valores de index desconhecido

# list_example.sort() - ordena a list_examplea sendo em ordem alfabética ou numérica
# list_example.sort(reverse=True) - ordena em ordem reversa
# Essas maneiras alteram a list_examplea existente

# sorted(list_example) - retorna uma list_examplea nova, bons hábitos criar uma list_examplea nova reversa
# sorted(list_example, reverse=True)

aux = list(enumerate(list_example)) # gera um dicionario valor posição da lista
print(aux) 

for i, j in aux:
    print(f'{i} | {j}')

 


