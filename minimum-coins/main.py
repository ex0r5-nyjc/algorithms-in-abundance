from typing import List, Tuple


def get_change(value: float, denomination: Tuple[float, ...]) -> List[float]:
    """
    Calculate the minimum number of coins needed to make up a value using greedy algorithm.

    Args:
        value: The target amount to make change for
        denomination: A tuple of available coin denominations (should be in descending order)

    Returns:
        A list of coin denominations used to make the change
    """
    # Write your code here
    pass


def get_change_limited(value: float, available_coins: List[float]) -> List[float]:
    """
    Calculate change when coins of each denomination are limited (not unlimited).

    Args:
        value: The target amount to make change for
        available_coins: A list of available coins (not unique denominations)

    Returns:
        A list of coin denominations used to make the change
    """
    # Write your code here
    pass


def get_change_recursive(value: int, denominations: Tuple[int, ...]) -> List[int]:
    """
    Calculate change using a recursive approach (works with integer amounts).

    Args:
        value: The target amount in cents (integer)
        denominations: A tuple of available coin denominations in cents

    Returns:
        A list of coin denominations used to make the change
    """
    # Write your code here
    pass


def count_coins(coins: List[float]) -> dict:
    """
    Count the number of each denomination used in the change.

    Args:
        coins: A list of coin denominations

    Returns:
        A dictionary with denomination as key and count as value
    """
    # Write your code here
    pass


def validate_change(coins: List[float], target_value: float) -> bool:
    """
    Validate that the provided coins sum to the target value.

    Args:
        coins: A list of coin denominations
        target_value: The expected total value

    Returns:
        True if the coins sum to the target value, False otherwise
    """
    # Write your code here
    pass
