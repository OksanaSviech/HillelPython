import string

users_input = input("Enter letters: ")
information = users_input.split("-")
start_letter = information[0]
end_letter = information[1]
result = str()

start_index = string.ascii_letters.index(start_letter)
end_index = string.ascii_letters.index(end_letter)

for letters in range(start_index, end_index + 1):
    result += string.ascii_letters[letters]

print(result)
