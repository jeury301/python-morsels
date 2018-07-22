def v0_multimax(iterable):
    """Return a list of all maximum values.

    One way to solve this problem is to loop through our iterable to find the
    maximum value and then loop through it again to find all values
    that are equal to it.
    """
    max_item = None
    for item in iterable:
        if max_item is None or item > max_item:
            max_item = item
    items = []
    for item in iterable:
        if item == max_item:
            items.append(item)
    return items

def v1_multimax(iterable):
    """Return a list of all maximum values.

    Using python's max function
    """
    max_item = max(iterable)
    items = []
    for item in iterable:
        if item == max_item:
            items.append(item)
    return items


def v2_multimax(iterable):
    """Return a list of all maximum values.

    Using a list comphrehension
    """
    max_item = max(iterable)
    return [
        item
        for item in iterable
        if item == max_item
    ]

def v3_multimax(iterable):
    """Return a list of all maximum values.

    Bonus 1: make sure our function returned an empty list when
    given an empty iterable.
    """
    max_item = None
    for item in iterable:
        if max_item is None or item > max_item:
            max_item = item
    return [
        item
        for item in iterable
        if item == max_item
    ]

def v4_multimax(iterable):
    """Return a list of all maximum values.

    Bonus 1 - on short solution.
    """
    try:
        max_item = max(iterable)
    except ValueError:
        return []
    return [
        item
        for item in iterable
        if item == max_item
    ]

def v5_multimax(iterable):
    """Return a list of all maximum values.

    Avoiding ValueError being raised by Max on empty lists - by specifying
    a default value.
    """
    max_item = max(iterable, default=None)
    return [
        item
        for item in iterable
        if item == max_item
    ]

def v6_multimax(iterable):
    """Return a list of all maximum values.

    Bonus 2: Make the function works with lazy iterables.

    Our current solutions fail this requirement because they loop through
    our iterable twice and generators can only be looped over one time only.

    We could keep track of the maximum values as we loop and manually build
    up a list of maximums
    """
    maximums = []
    for item in iterable:
        if not maximums or maximums[0] == item:
            maximums.append(item)
        elif item > maximums[0]:
            maximums = [item]
    return maximums

def v7_multimax(iterable):
    """Return a list of all maximum values.

    Or we could make a new list out of the given iterable and then find
    the max and loop over it again just as we did before
    """
    iterable = list(iterable)
    max_item = max(iterable, default=None)
    return [
        item
        for item in iterable
        if item == max_item
    ]

def v8_multimax(iterable, key=None):
    """Return a list of all maximum values.

    Bonus 3: accept a key argument which is a function that will determine
    how our values should be compared to each other
    """
    if key is None:
        def key(item): return item
    item_scores = [
        (key(item), item)
        for item in iterable
    ]
    try:
        max_key = max(score for score, _ in item_scores)
    except ValueError:
        return []
    return [
        item
        for score, item in item_scores
        if score == max_key
    ]

def v9_multimax(iterable, key=None):
    """Return a list of all maximum values.

    Looping over all the items and keeping track of the current maximum key
    and the current maximum items list and then updating the key and the list
    as we find new maximums
    """
    if key is None:
        def key(item): return item
    max_key = None
    maximums = []
    for item in iterable:
        k = key(item)
        if k == max_key:
            maximums.append(item)
        elif not maximums or k > max_key:
            maximums = [item]
            max_key = k
    return maximums

​def v10_multimax(iterable, key=lambda x: x):
    """Return a list of all maximum values.

    Defaulting key argument to a function.
    """
    max_key = None
    maximums = []
    for item in iterable:
        k = key(item)
        if k == max_key:
            maximums.append(item)
        elif not maximums or k > max_key:
            maximums = [item]
            max_key = k
    return maximums
