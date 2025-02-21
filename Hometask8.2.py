import string
def is_palindrome(text):
    lower_text = text.lower()
    without_string_punctuation = ''.join(ch for ch in lower_text if ch not in string.punctuation and ch != ' ')

    return without_string_punctuation == without_string_punctuation[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

