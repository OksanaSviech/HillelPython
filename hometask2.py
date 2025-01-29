user_input = int(input("Please enter a five-digit integer: "))
a = user_input//10000
b = (user_input//1000)%10
c = (user_input//100)%10
d = (user_input//10)%10
e = user_input % 10

print("Your reversed number:" ,e ,d ,c ,b ,a)
