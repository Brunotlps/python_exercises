number_1 = float(input("Type the first number: "))
number_2 = float(input("Type the second number: "))
# average = (number_1 + number_2) /  2
# print(f"The average of the two numbers is: {average}")


import statistics
numbers = [number_1, number_2]
best_average = statistics.mean(numbers)
print(f"The average of the two numbers is: {best_average}")