#1
lst = [12, 3, 4, 10, 8]
if len(lst) > 1:
    last_element = lst.pop()
    lst.insert(0, last_element)
print(lst)

# або
#2
lst_1 = [12, 3, 4, 10, 8]
if len(lst_1) > 1:
    last_element_1 = lst_1[-1]
    lst_1 = [last_element_1] + lst_1[:-1]

print(lst_1)
