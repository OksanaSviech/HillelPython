def difference(*args):
    if len(args) == 0:
        return 0
    else:
        max_num = max(args)
        min_num = min(args)
        return round(max_num - min_num, 2)

assert difference(1, 2, 3) == 2
assert difference(5, -5) == 10
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4
assert difference() == 0
print('OK')