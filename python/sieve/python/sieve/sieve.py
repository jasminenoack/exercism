def create_dictionary(num):
    nums = {}

    for i in range(2, num + 1):
        nums[i] = True

    return nums


def sieve(num):
    nums = create_dictionary(num)

    for n in nums:
        i = n

        if nums[n]:
            while i * n <= num:
                nums[i * n] = False
                i += 1

    return [n for n in nums if nums[n]]