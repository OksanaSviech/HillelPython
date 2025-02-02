#1 у списку парна кількість елементів
list1 = [1, 2, 3, 4, 5, 6]
middle_1 = (len(list1)+1)//2
new_list_1 = list1 [:middle_1]
new_list_2 = list1 [middle_1:]
result_list1 = [new_list_1,new_list_2]
print(result_list1)

#2 в списку непарна кількість елементів
list2 = [1, 2, 3, 4, 5, 6, 7]
middle_2 = (len(list2)+1)//2
new_list_3 = list2[:middle_2]
new_list_4 = list2[middle_2:]
result_list2 = [new_list_3, new_list_4]
print(result_list2)

#3 список порожній
list3 = []
middle_3 = (len(list3)+1)//2
new_list_5 = list3[:middle_3]
new_list_6 = list3[middle_3:]
result_list3 = [new_list_5,new_list_6]
print(result_list3)