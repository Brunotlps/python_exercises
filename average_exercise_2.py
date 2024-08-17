import statistics 

notas = []
nome = input("Informe o nome do aluno: ")
print()

for i in range (4):
    notas.append(float(input(f"Informe a {i + 1}° nota: ")))

media = statistics.mean(notas)
if media >= 6:
    print(f"Aluno: {nome} - média: {media} - status: 'Aprovado'")
elif media >= 4:
    print(f"Aluno: {nome} - média: {media} - status: 'Recuperação")
else:
    print(f"Aluno: {nome} - média: {media} - status: 'Reprovado")

