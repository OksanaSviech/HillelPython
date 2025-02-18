def common_elements():
    set_1 = set(i for i in range(101) if i % 3 == 0)
    set_2 = set(i for i in range(101) if i % 5 == 0)
    intersection_set = set_1.intersection(set_2)
    return intersection_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

