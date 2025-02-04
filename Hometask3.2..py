lst=[12, 3, 4, 10, 8]
if len(lst) == 0:
    lst = []
else:
    new_value = lst.pop()
    lst.insert(0, new_value)
print(lst)


lst_1 = []
if len(lst_1)==0:
    new_lst = []
else:
    new_lst = [lst_1[-1]] + lst_1[:-1]
print(new_lst)

