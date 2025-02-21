def add_one(some_list):
    number_string = [str(number) for number in some_list]
    string = ''.join(number_string)
    number_add = str(int(string) + 1)

    number_list = [int(i) for i in number_add]

    return number_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")