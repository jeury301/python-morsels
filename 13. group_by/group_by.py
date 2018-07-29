def default(n):
    return n

def group_by(numbers, key_func=default):
    """Return a dict-like object containing items in the list grouped by key.

    Args:
        numbers (iterator): items to group by key
        key_func (function): function to group items by

    Returns:
        Dictionary of numbers grouped by key_func
    """
    groups = {}
    for number in numbers:
        groups.setdefault(key_func(number), [])
        groups[key_func(number)].append(number)
    return groups

if __name__ == "__main__":
    grouped = group_by([1, 2, 1, 3, 2, 1])
    print(grouped)
