def lstrip(iterable, obj):
    """Removing leftmost items until condition by obj is not met.

    Args:
        iterable (iter): an iterable
        obj (object): an object to determine the condition to remove leftmost
                      items from iterable.

    Returns:
        the iterable with the leftmost items removed which meet the condition.
    """
    diff = False
    for x in iterable:
        if not det(x, obj):
            diff = True
        if det(x, obj) and not diff:
            continue
        else:
            yield x

def det(x, obj):
    if callable(obj):
        return obj(x)
    else:
        return x == obj
