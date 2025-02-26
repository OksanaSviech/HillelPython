def popular_words (text, words):
    new_text = text.lower().split()
    result_dict = {}

    for word in words:
        result_count = new_text.count(word)
        result_dict[word] = result_count
    return result_dict

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
