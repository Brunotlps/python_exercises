from collections import Counter


numbers = []

print("Type the numbers: ")

while True:
    aux_input = input()
    if aux_input == "":
        break

    try:
        numbers.append(aux_input)
    except ValueError:
        print("Please, enter a valid number")

aux_counter = Counter(numbers)

most_common = aux_counter.most_common(1)
print(most_common)

