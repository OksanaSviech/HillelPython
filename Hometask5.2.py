while True:
    first_number=float(input("Enter the first number: "))
    second_number=float(input("Enter the second number: "))
    action_sign=input("Enter the action sign (+,-.* or /): ")

    if action_sign == "+":
        print("Result:", first_number + second_number)
    elif action_sign == "-":(
        print("Result: ", first_number - second_number))
    elif action_sign == "*":\
        print("Result: ", first_number * second_number)
    elif action_sign == "/":
        if second_number == 0:
            print("You can't divide by zero")
        else:
            print("Result: ", first_number / second_number)
    else:
        print("Please, choose another action sign")

    while True:
        restart = input("Do you want to continue working with calculator (yes/y or no/n): ")
        if restart.lower() == 'yes' or restart.lower() == 'y':
            break
        elif restart.lower() == 'no' or restart.lower() == 'n':
            exit()
        else:
            print('Please, choose the answer (yes/y or no/n)')
