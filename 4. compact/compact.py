def compact_0(iterable):
    """Return new iterable with adjacent duplicate values removed."""
    deduped = []
    previous = object()
    for item in iterable:
        if item != previous:
            deduped.append(item)
            previous = item
    return deduped

def compact(iterable):
    from itertools import groupby

    return (
        item
        for item, group in groupby(iterable)
    )

print(compact([None, None, 3, 4]))