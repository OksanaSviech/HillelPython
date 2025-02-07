lst = [0, 1, 7, 2, 4, 8]

if len(lst) == 0:
    print('0')
else:
    result = sum(lst[::2]) * lst[-1]
    print(result)




# lst = [0, 1, 7, 2, 4, 8]
# sum_even_indices = 0
# if len(lst) == 0:
#     print('0')
# else:
#     for i in range(0, len(lst), 2):
#         sum_even_indices += lst[i]
#     result = sum_even_indices * lst[-1]
#     print(result)
