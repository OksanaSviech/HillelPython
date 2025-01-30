user_input = int(input("Please enter a five-digit integer: "))
first_num = user_input // 10000
second_num = (user_input // 1000) % 10
third_num = (user_input // 100) % 10
fourth_num = (user_input // 10) % 10
fifth_num = user_input % 10

reversed_number = fifth_num * 10000 + fourth_num * 1000 + third_num * 100 + second_num * 10 + first_num

print(reversed_number)

