user_input = int(input("Please enter a four-digit integer: "))
a = user_input//1000
b = (user_input//100)%10
c = (user_input//10)%10
d = user_input % 10
print("Your result is: ")
print(a)
print(b)
print(c)
print(d)
