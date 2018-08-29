from datetime import timedelta
from decimal import Decimal

def deep_add(to_add, start=0):
    """Adding up all numbers from a nested list of numbers
    """
    global sum
    global data_type

    data_type = Decimal
    sum = None
    d_deep_add(to_add)
    d_deep_add(start)

    if data_type == timedelta:
        return timedelta(sum)
    return sum

def d_deep_add(to_add):
    global sum, data_type

    try:
        for x in iter(to_add):
            d_deep_add(x)
    except TypeError as te:
        if type(to_add) == list:
            for x in to_add:
                d_deep_add(x)
        else:
            data_type = type(to_add)
            if type(to_add) == timedelta:
                to_add = to_add.days
            if not sum:
                sum = to_add
            else:
                sum += to_add

if __name__ == '__main__':
    print(deep_add([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]))
    print(deep_add([1, [2, [3, 4], [], [[5, 6], [7, 8]]]]))
    print(deep_add([[], []]))
