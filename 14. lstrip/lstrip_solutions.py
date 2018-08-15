def v0_lstrip(iterable, strip_value):
    """Return iterable with strip_value items removed from beginning."""
    stripped = []
    is_beginning = True
    for item in iterable:
        if is_beginning:
            if item != strip_value:
                is_beginning = False
            else:
                continue
        stripped.append(item)
    return stripped

def v1_lstrip(iterable, strip_value):
    """Return iterable with strip_value items removed from beginning."""
    stripped = []
    is_beginning = True
    for item in iterable:
        if is_beginning and item == strip_value:
            continue
        is_beginning = False
        stripped.append(item)
    return stripped

def v2_lstrip(iterable, strip_value):
    """Return iterable with strip_value items removed from beginning."""
    stripped = []
    iterator = iter(iterable)
    try:
        item = next(iterator)
        while item == strip_value:
            item = next(iterator)
        stripped.append(item)
    except StopIteration:
        pass
    else:
        for item in iterator:
            stripped.append(item)
    return stripped

def v3_lstrip(iterable, strip_value):
    """Return iterable with strip_value items removed from beginning."""
    stripped = []
    iterator = iter(iterable)
    for item in iterator:
        if not item == strip_value:
            stripped.append(item)
            break
    for item in iterator:
        stripped.append(item)
    return stripped

from itertools import dropwhile

def v4_lstrip(iterable, strip_value):
    """Return iterable with strip_value items removed from beginning."""
    stripped = []
    def is_strip_value(value): return value == strip_value
    for item in dropwhile(is_strip_value, iterable):
        stripped.append(item)
    return stripped

def v5_lstrip(iterable, strip_value):
    """Return iterable with strip_value items removed from beginning."""
    def is_strip_value(value): return value == strip_value
    return dropwhile(is_strip_value, iterable)

def v6_lstrip(iterable, strip_value):
    """Return iterable with strip_value items removed from beginning.

    Bonus 1: We're supposed to make lstrip return an iterator.
    """
    iterator = iter(iterable)
    for item in iterator:
        if item != strip_value:
            yield item
            break
    for item in iterator:
        yield item

def v6_lstrip(iterable, strip_value):
    """Return iterable with strip_value items removed from beginning."""
    iterator = iter(iterable)
    for item in iterator:
        if item != strip_value:
            yield item
            break
    yield from iterator

def v7_lstrip(iterable, strip_value):
    """Return iterable with strip_value items removed from beginning.

    Bonus 2: we're supposed to optionally accept a function as our strip value
    and call that function to determine whether values should be removed.
    """
    iterator = iter(iterable)
    for item in iterator:
        if (callable(strip_value) and not strip_value(item)
                or not callable(strip_value) and item != strip_value):
            yield item
            break
    yield from iterator

def v8_lstrip(iterable, strip_value):
    """Return iterable with strip_value items removed from beginning."""
    iterator = iter(iterable)
    if callable(strip_value):
        predicate = strip_value
    else:
        def predicate(value): return value == strip_value
    for item in iterator:
        if not predicate(item):
            yield item
            break
    yield from iterator

def v9_lstrip(iterable, strip_value):
    """Return iterable with strip_value items removed from beginning."""
    if callable(strip_value):
        predicate = strip_value
    else:
        def predicate(value): return value == strip_value
    return dropwhile(predicate, iterable)
