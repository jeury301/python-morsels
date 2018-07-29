def v0_uniques_only(sequence):
    """Return sequence in the same order but with duplicates removed.

    When you read that you're only supposed to return unique values,
    you might have thought to convert the incoming items to a set and then
    back to a list, to keep only the unique ones around...

    But this doesn't work consistently because sets are unordered!!
    """
    return list(set(sequence))

def v1_uniques_only(sequence):
    """Return sequence in the same order but with duplicates removed.

    You might have instead thought to use indexes to check items
    that came before the current item while looping...

    This will only work for sequences though.
    """
    items = []
    for i, item in enumerate(sequence):
        if item not in sequence[:i]:
            items.append(item)
    return items

def v2_uniques_only(iterable):
    """Return iterable in the same order but with duplicates removed.

    To get our function to work with all types of iterables,
    we'll need to keep track of all the items we've seen so far.
    We're actually already doing that with our items list.
    So we could simply check whether each new item is already
    contained in our list.

    This works but it's going to be very slow for large lists of items
    because checking for containment (X not in Y) in a list requires
    looping through the whole list.
    """
    items = []
    for item in iterable:
        if item not in items:
            items.append(item)
    return items

def v3_uniques_only(iterable):
    """Return iterable in the same order but with duplicates removed.

    We can make this faster by using a set...

    Sets rely on hashes for lookups so containment checks won't slow down as
    our hash grows in size. Notice we're building up both a list and a set
    but we're checking only the set for containment and returning only the list.
    We still need to make a list in addition to our set because sets are
    unordered by nature and we want the order of first appearance of each
    item to be maintained.
    """
    seen = set()
    items = []
    for item in iterable:
        if item not in seen:
            items.append(item)
            seen.add(item)
    return items

def v4_uniques_only(iterable):
    """Return iterable in the same order but with duplicates removed.

    If you're using Python 3.6+, you could also use dict.fromkeys to create
    a dictionary (which has unique keys that maintain insertion ordered as
    of Python 3.6) and then grab just the keys from the dictionary
    """
    return dict.fromkeys(iterable).keys()

def v5_uniques_only(iterable):
    """Return iterable in the same order but with duplicates removed.

    Bonus #1: Return a generator.

    We're using a generator function here.
    Generator functions are unlike regular functions.
    They return a generator object which will return items every time a
    yield statement is hit in our generator function.
    """
    seen = set()
    for item in iterable:
        if item not in seen:
            yield item
            seen.add(item)

def v6_uniques_only(iterable):
    """Return iterable in the same order but with duplicates removed.

    Bonus #2: want our function to work with non-hashable types

    we'll need to use something besides a set or a dictionary to
    store seen values.  We could use a list, like we did before...

    This works, but it will be slower.  Answering the question
    "item not in seen" when using a list requires iterating all
    the way through the list looking for a match.  A set can answer
    the same question without iterating at all.
    """
    seen = []
    for item in iterable:
        if item not in seen:
            yield item
            seen.append(item)

from collections.abc import Hashable

def v7_uniques_only(iterable):
    """Return iterable in the same order but with duplicates removed.

    The collections.abc.Hashable type uses duck typing when doing an
    isinstance check, so asking isinstance(item, Hashable) will always
    give us the correct answer for each object in Python.
    """
    seen_hashable = set()
    seen_unhashable = []
    for item in iterable:
        if isinstance(item, Hashable):
            if item not in seen_hashable:
                yield item
                seen_hashable.add(item)
        else:
            if item not in seen_unhashable:
                yield item
                seen_unhashable.append(item)

def v8_uniques_only(iterable):
    """Return iterable in the same order but with duplicates removed.

    Another way we could check for hashability is to simply try to add each
    item to the set and if it fails, add it to the list instead...

    This is practicing "it's easier to practice forgiveness than permission",
    which is a common programming practice in the Python world
    """
    seen_hashable = set()
    seen_unhashable = []
    for item in iterable:
        try:
            if item not in seen_hashable:
                yield item
                seen_hashable.add(item)
        except TypeError:
            if item not in seen_unhashable:
                yield item
                seen_unhashable.append(item)
