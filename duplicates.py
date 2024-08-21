def has_duplicates(lst):
    return len(lst) != len(set(lst))


numbers_list = []

while True:
    number = input("Enter a number: ")
    if number == "":
        break
    numbers_list.append(int(number))


if has_duplicates(numbers_list):
    print("The list has duplicates")
else:
    print("The list is ok")


