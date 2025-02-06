lst = [0, 1, 7, 2, 4, 8]
new_list = lst[::2]
last_value = lst.pop(-1)
result = sum(new_list) * last_value
print(result)
