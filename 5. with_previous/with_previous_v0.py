def with_previous(values, **kwargs):
    """Creates a generator from an iterator that returns a tuple 
    for each item in the iterator. The tuple will be of the format 
    (current item, previous item)

    Args:
        values: Iterator of integer values

    Returns:
        A generator without adjacent duplicates
    """
    # check that the iterator is not empty
    if values:
        # the iterator is not empty
        # if 'fillvalue' was passed as a keyword argument
        # its value will be assigned to prev, otherwise it will assign None
        prev = kwargs.get("fillvalue") 
        for val in values:
            # iterating through iterator
            # yielding a tuple with prev and current value
            yield (val, prev)
            # update prev
            prev = val
