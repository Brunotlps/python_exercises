number = int(input("Enter a number: "))

aux = 0

while aux <= number:
    if aux % 2 == 0:
        print(aux)
    aux+=1