def second_index(text, some_str):
    first_ind = text.find(some_str)
    second_ind = text.find(some_str, first_ind + len(some_str))
    if second_ind == -1:
        return None
    else:
        return second_ind

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
