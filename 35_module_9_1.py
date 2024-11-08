def apply_all_func(int_list, *functions):
    results = {}
    for el in functions:
        results.update({el.__name__: el(int_list)})
    return results

ints = [3, 4, 5, 6, 1, 9]

print(apply_all_func(ints, min, max, len, sum, sorted))