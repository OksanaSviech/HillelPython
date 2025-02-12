import string
import keyword

some_string = input('Enter some string: ')
custom_punctuation = string.punctuation.replace("_", "")
valid_name = True

if some_string[0].isdigit():
    valid_name = False
elif any(char.isupper() for char in some_string):
    valid_name = False
elif any(char in custom_punctuation for char in some_string):
    valid_name = False
elif " " in some_string:
    valid_name = False
elif some_string in keyword.kwlist:
    valid_name = False
elif some_string.startswith('__') :
    valid_name = False

if valid_name:
    print('True')
else:
    print('False')

