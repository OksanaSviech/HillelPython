lst = [12, 3, 4, 10, 8]
if len(lst) > 1:
    last_element = lst.pop()
    lst.insert(0, last_element)
print(lst)
