# Objective

This assignment is practice to be comfortable **implementing greedy algorithms and working with currency calculations**.

----------

# Minimum Coins: Making Change with Currency

A collection of available coin denominations is provided as `denomination`, a list of float values representing the value of each coin, sorted in descending order.

Given a `value`, determine the minimum number of coins needed from `denomination` such that their total is `value`.

## Task: Find Change for Value

Write a function `get_change(value: float, denomination: tuple) -> list` that returns a list of coin denominations needed to make up `value`. The returned list need not be in any particular order.

### Example Output

```python
denomination = (1.00, 0.50, 0.20, 0.10, 0.05, 0.01)
get_change(0.90, denomination)
# Output: [0.50, 0.20, 0.20]
```

<details>
<summary><b>Algorithm</b></summary>
<p>To solve this problem using a greedy approach, follow these steps:</p>
<ol>
  <li>Start with the largest denomination.</li>
  <li>Use as many coins of this denomination as possible without exceeding the target value.</li>
  <li>Move to the next smaller denomination and repeat.</li>
  <li>Continue until the exact value is reached.</li>
  <li>Return the list of coins used.</li>
</ol>
<p><strong>Note:</strong> The greedy algorithm works for most currency systems but may not always give the optimal solution for arbitrary denomination sets.</p>
</details>

<details>
<summary><b>Tips</b></summary>
<p>Be careful with floating-point arithmetic - consider using integers (working in cents) instead of floats to avoid precision issues.</p>
<p>The denominations should be sorted in descending order for the greedy algorithm to work correctly.</p>
<p>Make sure to handle edge cases like exact amounts and amounts that can't be made with the given denominations.</p>
</details>

<details>
<summary><b>Challenge</b></summary>
<p>- Assuming the number of coins of each denomination is not unlimited, given a list of available coins, determine the minimum number of coins needed.</p>
<p>- Example: `get_change_limited(0.90, [1.00, 0.20, 0.20, 0.20, 0.20, 0.20, 0.10, 0.10])` should return `[0.20, 0.20, 0.20, 0.20, 0.10]`.</p>
<p>- Implement a recursive solution instead of an iterative one.</p>
<p>- Implement a dynamic programming solution that always finds the optimal solution.</p>
</details>

----------

# Submission

Before submitting your code, run the automated tests on your functions. In the shell, type `python test_main.py` and press enter to see the results of the testing.
