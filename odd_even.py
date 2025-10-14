def classify_numbers(nums: list[int]) -> list[str]:
    """
    Classifies a list of numbers as "odd" or "even".

    Args:
        nums: A list of integers.

    Returns:
        A list of strings, where each string is "odd" or "even".
    """
    return ["even" if num % 2 == 0 else "odd" for num in nums]
