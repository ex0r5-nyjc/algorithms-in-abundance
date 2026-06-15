# Objective

This assignment is practice to be comfortable **implementing recursive backtracking algorithms**.

----------

# Sudoku Solver: Brute Force Recursive Algorithm

A "brute force" Sudoku solver tries all possible combinations by filling in blank spaces one by one. If it encounters a case that is obviously impossible, it backtracks by undoing the last step.

## Task: Implement a Recursive Brute-Force Sudoku Solver

A recursive function `solve()` for solving a 3×3 Sudoku puzzle carries out the following steps:

1. If the puzzle is complete and correct, `return puzzle`.
2. If the puzzle is complete but incorrect, `return None`.
3. If the puzzle is still incomplete, fill in the first unused value in the first unfilled slot.
4. Solve the puzzle again (recursive call).
5. If the result is `None`, no solution is possible. Undo Step 1 and try with the next value.
6. If the result is a puzzle, return it.
7. If all values have been tried, the puzzle is unsolvable (`return None`).

Some helper functions are provided:
- `generate()` to generate a puzzle.
- `get_unused()` to get a list of numbers that have not yet been used.
- `get_unfilled()` to get a list of coordinates that have not yet been filled.
- `is_complete()` to check if a puzzle is completely filled.
- `is_correct()` to check if a fully filled puzzle is correct.

### Function Signature

```python
def solve(original_puzzle: list) -> Optional[list]:
    '''
    Attempts to solve puzzle using recursive backtracking.
    Fills the first unfilled slot with the first unused value.
    If solution check passes, calls solve() recursively with the
        new puzzle.
    Else, tries first unfilled slot with the next value.

    Returns:
        puzzle if solved, None if unsolvable
    '''
```

<details>
<summary><b>Algorithm</b></summary>
<p>The recursive backtracking algorithm works as follows:</p>
<ol>
  <li><strong>Base case 1:</strong> If puzzle is complete and correct, return it (success).</li>
  <li><strong>Base case 2:</strong> If puzzle is complete but incorrect, return None (failure).</li>
  <li><strong>Recursive case:</strong> Find first unfilled slot and first unused value.</li>
  <li>Fill the slot with the value and recursively call solve().</li>
  <li>If recursive call returns None, undo the change and try next value.</li>
  <li>If recursive call returns a puzzle, propagate it up.</li>
  <li>If all values tried without success, return None.</li>
</ol>
<p><strong>Key insight:</strong> You only need two return values: the puzzle (success) or None (failure).</p>
</details>

<details>
<summary><b>Tips</b></summary>
<p>Use `deepcopy` to avoid modifying the original puzzle during exploration.</p>
<p>The function should only have two possible return values: `puzzle` or `None`.</p>
<p>Think through your decision table: when should you return puzzle vs None?</p>
<p>Hint 1: You don't need to fill all unfilled slots - subsequent recursive calls will handle them.</p>
<p>Hint 2: Focus on just the first unfilled slot and first unused value in each call.</p>
</details>

<details>
<summary><b>Challenge</b></summary>
<p>- Improve the time efficiency of the algorithm (e.g., by trying values in a smarter order).</p>
<p>- Write a `while`-loop implementation of the 3×3 solver.</p>
<p>- Write a 9×9 Sudoku solver using the same principles.</p>
<p>- Add constraint propagation to reduce the search space.</p>
</details>

----------

# Submission

Before submitting your code, run the automated tests on your functions. In the shell, type `python test_main.py` and press enter to see the results of the testing.
