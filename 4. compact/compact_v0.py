def compact(values):
    """Creates a generator (that can be iterated using next()), from a list of
    values, avoiding any adjacent duplicates

    Args:
        values: Iterator of integer values

    Returns:
        A generator without adjacent duplicates
    """

    # check that the iterator is not empty
    if values:
        # the iterator is not empty
        curr = object() # use to keep track of the current (previous value)
        for val in values:
            # iterating through iterator
            if curr != val:
                # adjacent values are different, yield this value too
                yield val
            # update current
            curr = val

gen = compact([None, None, 2, 3])
while True:
    try:
        print(next(gen))
    except StopIteration:
        break
