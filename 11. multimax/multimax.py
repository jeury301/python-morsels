from collections import Counter
def multimax(k, key=None):
    """Returns an in-place list of the max values in the k.

    Args:
        k(lazy iteration, generator or list): contains the list of items
        key: a key by which to sort the items

    Returns:
        A list of the max values in the input.
    """
    p = list(k)[:]
    if not p: return []
    if key:
        return [x for x in p if key(x) == key(sorted(p, key=key)[::-1][0])]
    return [x for x in p if x == sorted(p, key=key)[::-1][0]]

if __name__ == "__main__":
    name = ["jeury-", "miguel", "mejia-"]
    print(multimax(name,key=len))
