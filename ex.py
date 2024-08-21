idades = [25, 30, 35, 40, 45]
idades.append(50)
print(f'soma = {sum(idades)}')

print(f'media = {float(sum(idades) / len(idades))}')

print(f'idade máxima: {max(idades)}')
print(f'idade mínima: {min(idades)}')

print(f'lista reordenada: {sorted(idades, reverse=True)}')