first_number = input("Enter the first number: ")

if first_number[0] == '-' and (first_number[1:].isdigit() or '.' in first_number[1:]):
    if '.' in first_number:
        first_number = float(first_number)
    else:
        first_number = int(first_number)
elif first_number.isdigit() or '.' in first_number:
    if '.' in first_number:
        first_number = float(first_number)
    else:
        first_number = int(first_number)
else:
    print("Input correct data: the first number is incorrect")
    first_number = None

if first_number is not None:
    second_number = input("Enter the second number: ")
    if second_number[0] == '-' and (second_number[1:].isdigit() or '.' in second_number[1:]):
        if '.' in second_number:
            second_number = float(second_number)
        else:
            second_number = int(second_number)
    elif second_number.isdigit() or '.' in second_number:
        if '.' in second_number:
            second_number = float(second_number)
        else:
            second_number = int(second_number)
    else:
        print("Input correct data: the second number is incorrect")
        second_number = None

if first_number is not None and second_number is not None:
    action_sign = input("Enter the action sign (+, -, *, or /): ")

    if action_sign == "+":
        print("Result:", first_number + second_number)
    elif action_sign == "-":
        print("Result:", first_number - second_number)
    elif action_sign == "*":
        print("Result:", first_number * second_number)
    elif action_sign == "/":
        if second_number == 0:
            print("You can't divide by zero")
        else:
            print("Result:", first_number / second_number)
    else:
        print("Please, choose another action sign")
