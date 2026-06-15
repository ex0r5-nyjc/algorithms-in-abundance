from typing import Optional, List, Tuple
from copy import deepcopy


def generate() -> list:
    """
    Generate a 3x3 Sudoku puzzle with some cells pre-filled.

    Returns:
        A 3x3 puzzle represented as a list of lists, where None represents empty cells
    """
    # Sample 3x3 puzzle (incomplete)
    puzzle = [
        [None, 3, None],
        [None, None, 7],
        [9, None, None]
    ]
    return puzzle


def get_unused(puzzle: list) -> list:
    """
    Get a list of numbers (1-9) that have not yet been used in the puzzle.

    Args:
        puzzle: A 3x3 Sudoku puzzle

    Returns:
        A list of unused numbers from 1-9
    """
    # Find all used numbers in the puzzle
    used = set()
    for row in puzzle:
        for cell in row:
            if cell is not None:
                used.add(cell)

    # Return all numbers from 1-9 that are not used
    return [num for num in range(1, 10) if num not in used]


def get_unfilled(puzzle: list) -> list:
    """
    Get a list of coordinates that have not yet been filled.

    Args:
        puzzle: A 3x3 Sudoku puzzle

    Returns:
        A list of (row, col) tuples for cells that are None
    """
    unfilled = []
    for row_idx in range(3):
        for col_idx in range(3):
            if puzzle[row_idx][col_idx] is None:
                unfilled.append((row_idx, col_idx))
    return unfilled


def is_complete(puzzle: list) -> bool:
    """
    Check if a puzzle is completely filled (no None values).

    Args:
        puzzle: A 3x3 Sudoku puzzle

    Returns:
        True if puzzle is complete, False otherwise
    """
    for row in puzzle:
        for cell in row:
            if cell is None:
                return False
    return True


def is_correct(puzzle: list) -> bool:
    """
    Check if a fully filled puzzle is correct.

    For a 3x3 puzzle, this means:
    - All rows contain distinct numbers 1-9 (but for 3x3, we just check no duplicates)
    - Actually, for 3x3: each number 1-9 should appear exactly once

    Args:
        puzzle: A 3x3 Sudoku puzzle

    Returns:
        True if puzzle is correct, False otherwise
    """
    if not is_complete(puzzle):
        return False

    # For 3x3, we just need all numbers 1-9 to appear exactly once
    all_numbers = []
    for row in puzzle:
        for cell in row:
            all_numbers.append(cell)

    # Check we have exactly 9 cells
    if len(all_numbers) != 9:
        return False

    # Check all numbers 1-9 appear exactly once
    return sorted(all_numbers) == list(range(1, 10))


def solve(original_puzzle: list) -> Optional[list]:
    """
    Attempts to solve puzzle using recursive backtracking.

    Fills the first unfilled slot with the first unused value.
    If solution check passes, calls solve() recursively with the new puzzle.
    Else, tries first unfilled slot with the next value.

    Args:
        original_puzzle: A 3x3 Sudoku puzzle to solve

    Returns:
        The solved puzzle if successful, None if unsolvable
    """
    # Make a copy to avoid modifying the original
    puzzle = deepcopy(original_puzzle)

    # Step 1 & 2: Check if puzzle is complete
    if is_complete(puzzle):
        if is_correct(puzzle):
            return puzzle  # Step 1: Success!
        else:
            return None   # Step 2: Failed

    # Step 3: Find first unused value and first unfilled coordinate
    unused = get_unused(puzzle)
    unfilled = get_unfilled(puzzle)

    if not unused or not unfilled:
        return None  # Should not happen if puzzle is incomplete

    first_unused = unused[0]
    y, x = unfilled[0]  # First unfilled coordinate

    # Try each unused value
    while unused:
        test_value = unused.pop(0)  # Get first unused value

        puzzle[y][x] = test_value   # Step 3: Fill the slot

        result = solve(puzzle)      # Step 4: Recursive call

        if result is None:
            # Step 5: Undo and try next value
            puzzle[y][x] = None
            # Continue to next iteration of while loop
        else:
            # Step 6: Success! Return the solution
            return result

    # Step 7: All values tried, no solution found
    return None


def solve_iterative(puzzle: list) -> Optional[list]:
    """
    Solve puzzle using iterative approach instead of recursive.

    Args:
        puzzle: A 3x3 Sudoku puzzle to solve

    Returns:
        The solved puzzle if successful, None if unsolvable
    """
    # Write your code here for the challenge
    pass


def solve_9x9(puzzle: list) -> Optional[list]:
    """
    Solve a 9x9 Sudoku puzzle using the same principles.

    Args:
        puzzle: A 9x9 Sudoku puzzle to solve

    Returns:
        The solved puzzle if successful, None if unsolvable
    """
    # Write your code here for the challenge
    pass
