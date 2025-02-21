def find_unique_value(some_list):
   occurrences = {}
   for element in some_list:
       count = some_list.count(element)
       occurrences[element] = count

   for key, val in occurrences.items():
       if val == 1:
           return key
   return None

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
