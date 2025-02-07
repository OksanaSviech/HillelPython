lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
zero_list=[]

for x in lst:
    if x == 0:
        lst.remove(0)
        zero_list.append(0)

new_list = lst + zero_list

print(new_list)
