
numbers = []

for i in range (3):
    numbers.append(float(input(f"Type the {i + 1}° number: ")))

greatest_number = 0
for number in numbers:
    if number > greatest_number:
        greatest_number = number 

print(f"The greatest number is - {greatest_number}")