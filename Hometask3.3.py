#1
list1 = [1, 2, 3, 4, 5, 6]
new_list_1 = list1 [:3]
new_list_2 = list1 [3:]
result_list1 = [new_list_1,new_list_2]
print(result_list1)

list1 = [1, 2, 3, 4, 5, 6]
middle_1 = (len(list1)+1)//2
new_list_1 = list1 [:middle_1]
new_list_2 = list1 [middle_1:]
result_list1 = [new_list_1,new_list_2]
print(result_list1)

#2
list2 = [1, 2, 3, 4, 5]
new_list_3 = list2[:3]
new_list_4 = list2[3:5]
result_list2 = [new_list_3, new_list_4]
print(result_list2)

list2 = [1, 2, 3, 4, 5, 6, 7]
middle_2 = (len(list2)+1)//2
new_list_3 = list2[:middle_2]
new_list_4 = list2[middle_2:]
result_list2 = [new_list_3, new_list_4]
print(result_list2)

#3
list3 = []
new_list_4 = list3[:]
new_list_5 = list3[:]
result_list3 = [new_list_4,new_list_5]
print(result_list3)

list3 = []
middle_3 = (len(list3)+1)//2
new_list_4 = list3[:middle_3]
new_list_5 = list3[middle_3:]
result_list3 = [new_list_4,new_list_5]
print(result_list3)
