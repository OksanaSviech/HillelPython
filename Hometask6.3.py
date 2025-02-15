number = int(input("Enter the number: "))

while number > 9:
    additions = [int (addition) for addition in str(number)]
    result = 1
    for multipliers in additions:
        result *= multipliers
        number = result
print(number)
