first_number=float(input("Enter the first number: "))
second_number=float(input("Enter the second number: "))
action_sign=input("Enter the action sign (+,-.* or /): ")

if action_sign == "+":
    print("Result:", first_number + second_number)
elif action_sign == "-":
    print("Result: ", first_number - second_number)
elif action_sign == "*":
    print("Result: ", first_number * second_number)
elif action_sign == "/":
    if second_number == 0:
        print("You can't divide by zero")
    else:
        print("Result: ", first_number / second_number)
else:
    print("Please, choose another action sign")



