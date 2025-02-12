import string
sentence = input('Enter your sentence: ')
hashtag_sign = '#'
title_words = sentence.title()
without_string_punctuation = ''.join(ch for ch in title_words if ch not in string.punctuation and ch != ' ')
hashtag_add = hashtag_sign + without_string_punctuation
new_sentence = hashtag_add[:140]
print(new_sentence)
