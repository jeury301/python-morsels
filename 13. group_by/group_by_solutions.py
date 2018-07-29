from collections import defaultdict
from itertools import groupby

def v0_group_by(iterable, key_func):
    """Group iterable by key_func.

    The simplest way to write the group_by function is to use a dictionary
    and an if statement.  As we loop over the items in our iterable,
    we can check whether each item has a key in our dictionary or not.
    If the key in not yet in our dictionary, we'll add it with an empty
    list as the value.  We'll always append to the list as we loop.
    """
    groups = {}
    for item in iterable:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

def v1_group_by(iterable, key_func):
    """Group iterable by key_func.

    We could also use the get method to both get the list or default
    the list to an empty list and then assign back to the same key,
    That's a bit messy though.  There's not really an elegant way to
    refactor that to one line while still using the get method unless
    we stopped appending and started making a new list every time,
    which wouldn't be very efficient.
    """
    groups = {}
    for item in iterable:
        key = key_func(item)
        groups[key] = groups.get(key, [])
        groups[key].append(item)
    return groups

def v2_group_by(iterable, key_func):
    """Group iterable by key_func.

    The setdefault method was invented for dictionaries to solve just
    this situation.

    The setdefault method does two things: it returns the value for the given
    key from the dictionary and sets the value to the given key (an empty list)
    if the key isn't set yet.  So the append is appending to either the new
    empty list or the existing value at that key.

    I rarely use the setdefault method because I often find that it does a
    lot all at once and it doesn't make things any more clear than using
    an if statement.
    """
    groups = {}
    for item in iterable:
        key = key_func(item)
        groups.setdefault(key, []).append(item)
    return groups


def v3_group_by(iterable, key_func):
    """Group iterable by key_func.

    This defaultdict object is kind of cool.  Whenever a missing
    key is accessed, defaultdict will call the callable that was given
    to it (list in this case) and use the return value as the new value
    for that key.

    Notice that with both the setdefault method and with defaultdict
    we only need to reference the key once.  With defaultdict,
    our code line is so short it makes sense to put the key_func(item)
    access all on one line.

    So groups[key_func(item)] defaults to setting the given key to an empty
    list and whatever list we get back we can then append to.
    """
    groups = defaultdict(list)
    for item in iterable:
        groups[key_func(item)].append(item)
    return groups


def v4_group_by(iterable, key_func):
    """Group iterable by key_func.

    While searching for ways of grouping things in Python,
    you might have discovered the groupby utility in the itertools module.
    This works for grouping things, but it only works when our
    items-to-be-grouped are all consecutive.  We could try to still use
    it if we sort our items by their keys first
    """
    groups = {}
    iterable = sorted(iterable, key=key_func)
    for key, items in groupby(iterable, key=key_func):
        groups[key] = list(items)
    return groups

def v5_group_by(iterable, key_func):
    """Group iterable by key_func.

    You might notice that we could use a dictionary comprehension here
    """
    iterable = sorted(iterable, key=key_func)
    return {key: list(items) for key, items in groupby(iterable, key=key_func)}

def v6_group_by(iterable, key_func=None):
    """Group iterable by key_func.

    Bonus: make the key function argument optional.

    That lambda thing makes an anonymous function.
    An anonymous function is a function that doesn't have a name.
    You can create anonymous functions and then immediately pass them
    around without assigning a variable name to them.
    """
    groups = defaultdict(list)
    if key_func is None:
        key_func = lambda x: x
    for item in iterable:
        groups[key_func(item)].append(item)
    return groups

def v7_group_by(iterable, key_func=None):
    """Group iterable by key_func.

    PEP8, the Python style guide, says that we should never write
    "key_func = lamdba x: x".  Specifically it says that if we're using
    lambda to make a function and then assign it to a variable,
    we should use a def statement to make a function instead
    """
    groups = defaultdict(list)
    if key_func is None:
        def key_func(x): x
    for item in iterable:
        groups[key_func(item)].append(item)
    return groups

def v8_group_by(iterable, key_func=lambda x: x):
    """Group iterable by key_func.

    We can actually take this a little further though.
    Instead of defaulting key_func to None we could default it to a function.
    We'll use a lambda expression since that allows us to do this on one line.
    """
    groups = defaultdict(list)
    for item in iterable:
        groups[key_func(item)].append(item)
    return groups
