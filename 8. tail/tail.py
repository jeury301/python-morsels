def tail(real_iter, n_th):
    """Returns the last nth elements of an iterable.

    Takes any iterable and returns its lasth  nth items from the iterable/list.

    Args:
        real_iter: an interable or a list (iterable or list)
        n_th: nth number of items to return (int)

    Returns:
        A list containing the last nth items
    """
    if n_th <= 0:
        return []

    real_list = list(real_iter)
    start = len(real_list)-n_th if n_th < len(real_list) else 0
    return real_list[start:]

