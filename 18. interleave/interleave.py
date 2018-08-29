def interleave(iter_one, iter_two):
    for x, y in zip(iter_one, iter_two):
        yield x
        yield y

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(interleave(nums, (n**2 for n in nums)))
