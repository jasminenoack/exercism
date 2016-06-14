def find_nums(num, factors):
    return any(num % f == 0 for f in factors if f != 0)


def sum_of_multiples(num, factors=[3, 5]):
    return sum(filter(lambda x: find_nums(x, factors), range(1, num)))