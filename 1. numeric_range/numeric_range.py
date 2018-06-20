def numeric_range(numbers):
    """Calculates the difference between the min and max of a given list

    Args:
        numbers: A list of numbers

    Returns:
        The distance of the minimax
    """
    numbers = sorted(list(numbers))
    return (numbers[len(numbers) - 1] - numbers[0]) if numbers else 0
