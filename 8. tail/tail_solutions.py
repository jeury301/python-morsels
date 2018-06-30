def v0_tail(sequence, n):
    """Return the last n items of given sequence.

    But this won't pass all our tests. For one thing, the return value will be
    the same as the given sequence type. So if the given sequence is a string
    then we'll get a string returned and if it's a tuple then we'll get a
    tuple returned.
    """
    return sequence[-n:]

def v1_tail(sequence, n):
    """Return the last n items of given sequence.

    This works for non-lists but it doesn't when the given n is 0. This is
    because sequence[-0:] is the same thing as sequence[0:] and that will
    return the entire sequence (which is likely not 0 items)
    """
    return list(sequence[-n:])

def v2_tail(sequence, n):
    """Return the last n items of given sequence.

    This fixes the previous problem...
    """
    if n == 0:
        return []
    return list(sequence[-n:])

def v3_tail(sequence, n):
    """Return the last n items of given sequence.

    For the first bonus we're also supposed to make sure our tail function
    returns an empty list when the given n is negative. That should be as easy
    as changing the == sign to a <= sig/
    """
    if n <= 0:
        return []
    return list(sequence[-n:])

def v4_tail(iterable, n):
    """Return the last n items of given iterable.

    For the second bonus we were supposed to make our function work with any
    kind of iterable. We could just convert the incoming iterable to a listself.

    But this might not be a good idea. If someone calls our function with a
    very large iterable, we'll make a copy of that very large iterable and then
    give them back just the last n items of it. This might not seem like a huge
    problem to copy thousands of elements, but imagine if we were looping over
    lines in a 20GB log file and storing every line in memory. That would be
    pretty memory inefficient.
    """
    sequence = list(iterable)
    if n <= 0:
        return []
    return sequence[-n:]

def v5_tail(iterable, n):
    """Return the last n items of given iterable.

    Instead of storing every item in the given iterable into a new sequence,
    we could store just the last n items we've seen.

    Here we're using a * to unpacking the last (n-1) items into a new list
    with our current item at the end and then reassigning that to items.
    This use of * expressions only works in Python 3.5+.

    Note that this doesn't work when n is 1. When n is 1, (n-1) will be 0 which
    means our items list will grow continually instead of only keeping the
    last 1 item.
    """
    items = []
    if n <= 0:
        return []
    for item in iterable:
        items = [*items[-(n-1):], item]
    return items

def v6_tail(iterable, n):
    """Return the last n items of given iterable.

    We could fix this by doing something different in our loop whenever n is 1.

    This might look a little silly/repetitive but it works.
    """
    items = []
    if n <= 0:
        return []
    for item in iterable:
        if n == 1:
            items = [item]
        else:
            items = [*items[-n+1:], item]
    return items

def v7_tail(iterable, n):
    """Return the last n items of given iterable.

    We could move that if-else statement before our for loop by sticking
    our whole for loop inside it.

    This is likely more efficient for large iterables (because that condition
    isn't checked in each iteration of our loop) but it also looks a bit
    repetitive.
    """
    items = []
    if n == 1:
        for item in iterable:
            items = [item]
    elif n > 0:
        for item in iterable:
            items = [*items[-n+1:], item]
    return items

def v8_tail(iterable, n):
    """Return the last n items of given iterable.

    We can actually move that if-else outside of our for loop without repeating
    our loop if we pass in slice objects in our for loop...

    You don't see slice objects used much directly in Python.
    A slice object is what Python creates when you use the slicing notation.
    When you say sequence[-n:], Python essentially converts that to
    sequence[slice(-n, None)].
    """
    items = []
    if n <= 0:
        return []
    elif n == 1:
        index = slice(0, 0)
    else:
        index = slice(-(n-1), None)
    for item in iterable:
        items = [*items[index], item]
    return items

from collections import deque

def v9_tail(iterable, n):
    """Return the last n items of given iterable.

    This solution uses deque, a double-ended queue class, from the
    collections module...

    We're setting the maximum size of our deque to n. When you append to a
    deque which has reached it's maximum length, it will efficiently remove
    the item closest to the beginning before appending the new item.
    So this is an efficient way to keep track of the most recent
    n items we've seen.
    """
    if n <= 0:
        return []
    items = deque(maxlen=n)
    for item in iterable:
        items.append(item)
    return list(items)

def v10_tail(iterable, n):
    """Return the last n items of given iterable.

    So we're maxing a deque with our iterable and setting the maximum length
    (we could have used a positional argument but we chose to use a named
    one instead) and then converting that deque to a list so that our
    tests (which expect a list) pass.
    """
    if n <= 0:
        return []
    return list(deque(iterable, maxlen=n))
