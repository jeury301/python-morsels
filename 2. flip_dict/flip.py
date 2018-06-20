def flip_dict_of_lists(dict_to_flip, dict_type=None, key_func=None):
    """Flipping a dictionary of lists, with optional parameters to specify
    the type of dictionary and a normalization function to apply to all keys

    Args:
        dict_to_flip: Dictionary of lists to flip
        dict_type: Optional type of dictionary
        key_func: Optional function to apply to all keys

    Returns:
        A flipped dictionary
    """

    flipped_dict = {}

    for key in dict_to_flip:
        elements = dict_to_flip[key]
        
        for elem in elements:
            if flipped_dict.get(elem) is None:
                if key_func:
                    elem = key_func(elem)
                flipped_dict[elem] = []
            flipped_dict.get(elem).append(key)

    if dict_type:
        return dict_type(flipped_dict)

    return flipped_dict



