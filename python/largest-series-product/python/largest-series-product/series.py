from copy import deepcopy


def slices(string, set_size):
    result = []
    current_set = []

    if len(string) < set_size or set_size == 0:
        raise ValueError

    for char in string:
        current_set.append(int(char))

        if len(current_set) > set_size:
            current_set.pop(0)

        if len(current_set) == set_size:
            result.append(deepcopy(current_set))

    return result


def largest_product(string, set_size):
    if string == "":
        return 1
    
    largest = 0
    all_sets = slices(string, set_size)

    for nums in all_sets:
        product = reduce(lambda x, y: x * y, nums)
        if product > largest:
            largest = product

    return largest