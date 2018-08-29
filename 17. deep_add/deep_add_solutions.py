def v0_deep_add(list_or_number):
    """Return sum of values in given list, iterating deeply."""
    total = 0
    if type(list_or_number) == list:
        for x in list_or_number:
            total += deep_add(x)
        return total
    else:
        return list_or_number

def v1_deep_add(lists):
    """Return sum of values in given list, iterating deeply."""
    total = 0
    lists = list(lists)
    while lists:
        item = lists.pop()
        if isinstance(item, list):
            lists.extend(item)
        else:
            total += item
    return total

def v2_deep_add(list_or_number):
    """Return sum of values in given list, iterating deeply."""
    if type(list_or_number) == list:
        return sum(deep_add(x) for x in list_or_number)
    else:
        return list_or_number

def v3_deep_add(list_or_number):
    """Return sum of values in given list, iterating deeply."""
    return (
        sum(deep_add(x) for x in list_or_number)
        if type(list_or_number) == list
        else list_or_number
    )

def v4_deep_add(iterable_or_number):
    """Return sum of values in given iterable, iterating deeply."""
    try:
        return sum(deep_add(x) for x in iterable_or_number)
    except TypeError:
        return iterable_or_number

def v5_deep_add(iterable_or_number):
    """Return sum of values in given iterable, iterating deeply."""
    if isinstance(iterable_or_number, (int, float, complex)):
        return iterable_or_number
    else:
        return sum(deep_add(x) for x in iterable_or_number)

from numbers import Number

def v6_deep_add(iterable_or_number):
    """Return sum of values in given iterable, iterating deeply."""
    if isinstance(iterable_or_number, Number):
        return iterable_or_number
    else:
        return sum(deep_add(x) for x in iterable_or_number)

def v7_deep_add(iterable_or_number, start=0):
    """Return sum of values in given iterable, iterating deeply."""
    if isinstance(iterable_or_number, Number):
        return iterable_or_number
    else:
        total = start
        for x in iterable_or_number:
            total += deep_add(x)
        return total

def v8_deep_add(iterable_or_number, start=0):
    """Return sum of values in given iterable, iterating deeply."""
    if isinstance(iterable_or_number, Number):
        return iterable_or_number
    else:
        return sum((deep_add(x) for x in iterable_or_number), start)

def v9_deep_add(iterable_or_number, start=0):
    """Return sum of values in given iterable, iterating deeply."""
    try:
        iter(iterable_or_number)
    except TypeError:
        return iterable_or_number
    else:
        return sum((deep_add(x) for x in iterable_or_number), start)

def v10_deep_add(iterable_or_number, start=0):
    """Return sum of values in given iterable, iterating deeply."""
    if hasattr(iterable_or_number, '__iter__'):
        return sum((deep_add(x) for x in iterable_or_number), start)
    else:
        return iterable_or_number

from collections.abc import Iterable

def v11_deep_add(iterable_or_number, start=0):
    """Return sum of values in given iterable, iterating deeply."""
    if isinstance(iterable_or_number, Iterable):
        return sum((deep_add(x) for x in iterable_or_number), start)
    else:
        return iterable_or_number
