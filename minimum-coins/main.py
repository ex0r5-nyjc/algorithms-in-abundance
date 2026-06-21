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
    change = []
    temp = value
    prec = 0
    for coin in denomination:
        ls = str(coin).split(".")
        if len(ls) == 2 and len(ls[1]) > prec:
            prec = len(ls[1])
    mult = 10 ** prec
    temp = int(temp * mult)
    for coin in denomination:
        coin = int(coin * mult)
        div, mod = divmod(temp, coin)
        temp = mod
        for i in range(div):
            change.append(coin / mult)
        if temp == 0:
            break
    return change


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
    change = []
    temp = value
    prec = 0
    for coin in available_coins:
        ls = str(coin).split(".")
        if len(ls) == 2 and len(ls[1]) > prec:
            prec = len(ls[1])
    mult = 10 ** prec
    temp = int(temp * mult)
    for coin in available_coins:
        coin = int(coin * mult)
        if temp >= coin:
            temp -= coin
            change.append(coin / mult)
        if temp == 0:
            break
    return change


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
    temp = value
    if temp == 0 or len(denominations) == 0:
        return []
    add = None
    if temp >= denominations[0]:
        temp -= denominations[0]
        add = denominations[0]
        new_input = denominations
    else:
        new_input = denominations[1:]
    change = get_change_recursive(temp, new_input)
    if add != None:
        change.append(add)
    return change



def count_coins(coins: List[float]) -> dict:
    """
    Count the number of each denomination used in the change.

    Args:
        coins: A list of coin denominations

    Returns:
        A dictionary with denomination as key and count as value
    """
    # Write your code here
    output = {}
    for coin in coins:
        if coin in output.keys():
            output[coin] += 1
        else:
            output[coin] = 1
    return output


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
    inputsum = 0
    prec = 0
    for coin in coins:
        ls = str(coin).split(".")
        if len(ls) == 2 and len(ls[1]) > prec:
            prec = len(ls[1])
    mult = 10 ** prec
    for coin in coins:
        inputsum += int(coin * mult)
    return inputsum == int(target_value * mult)

if __name__ == "__main__":
    breakpoint()
    print(get_change(0.25, [1.00, 0.50, 0.20, 0.10, 0.05, 0.01]))
    print(get_change_limited(0.90, [1.00, 0.20, 0.20, 0.20, 0.20, 0.20, 0.10, 0.10]))
    print(get_change_recursive(67, (100, 50, 25, 10, 5, 1)))
    print(validate_change((0.5, 0.1, 0.05, 0.03, 0.01, 0.01),0.7))