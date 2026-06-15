# Objective

This assignment is practice to be comfortable **implementing algorithms for real-world printing layouts**.

----------

# Booklet Layout: Page Order for Printing Booklets

When printing pages that are meant to be stapled at the corner, we can just follow the usual order of pages: 1, 2, 3, 4, …

However, when printing a booklet, the order of pages is different.

## How Booklets Work

In each booklet, the first page must be printed with the last page, the 2nd page must be printed with the second-last page, and so on. Each piece of paper will have 4 pages printed on it (2-sided).

**Example**: For an 8-page booklet, the pages are arranged so that when folded:
- Page 1 prints with page 8
- Page 2 prints with page 7
- Page 3 prints with page 6
- Page 4 prints with page 5

## Task: Generate Page Order for Booklet Printing

Write a function `booklet_pages(n: int) -> list` that generates the page order for printing a booklet.

### Function Requirements

- Given `n`, the number of pages to be printed in the booklet (including cover and last page)
- Generate the page order in which the pages are to be printed
- If the number of pages is not a multiple of 4, the last few pages will be blank
- Blank pages should be represented with a `None` value

### Example Output

```python
>>> booklet_pages(8)
[8, 1, 2, 7, 6, 3, 4, 5]

>>> booklet_pages(14)
[None, 1, 2, None, 14, 3, 4, 13, 12, 5, 6, 11, 10, 7, 8, 9]
```

### Understanding the Output

The output represents the order pages should be sent to the printer:

**For 8 pages**: `[8, 1, 2, 7, 6, 3, 4, 5]`
- First sheet: pages 8 and 1 on front, pages 2 and 7 on back
- Second sheet: pages 6 and 3 on front, pages 4 and 5 on back

**For 14 pages**: `[None, 1, 2, None, 14, 3, 4, 13, 12, 5, 6, 11, 10, 7, 8, 9]`
- Notice the `None` values for blank pages since 14 is not divisible by 4
- The algorithm ensures proper folding and alignment

## Algorithm Approach

1. **Calculate the number of sheets needed**
   - Each sheet holds 4 pages (2 per side)
   - Round up to the next multiple of 4

2. **Generate page pairs**
   - First page pairs with last page
   - Second page pairs with second-last page
   - Continue until all pages are paired

3. **Handle odd numbers of pages**
   - Insert `None` for missing pages
   - Ensure the total length is divisible by 4

4. **Build the result list**
   - Follow the printer spread pattern
   - Ensure pages will align correctly when folded

## Implementation Hints

```python
def booklet_pages(n: int) -> list:
    """
    Generate page order for booklet printing.

    Args:
        n: Number of pages in the booklet

    Returns:
        List of page numbers in printing order (None for blank pages)
    """
    # Calculate the number of sheets needed
    # Each sheet has 4 pages, so round up to nearest multiple of 4
    total_pages = ((n + 3) // 4) * 4

    result = []

    # Your algorithm here
    # Think about how pages pair up:
    # - First with last
    # - Second with second-last
    # - etc.

    return result
```

## Additional Functions to Implement

### Function 1: validate_booklet_layout(page_order: list) -> bool

Validate that a booklet layout is correct.

```python
def validate_booklet_layout(page_order: list) -> bool:
    """
    Validate that a booklet layout will fold correctly.

    Returns: True if layout is valid, False otherwise
    """
    # Your code here
    pass
```

### Function 2: count_sheets(n: int) -> int

Calculate how many sheets of paper are needed.

```python
def count_sheets(n: int) -> int:
    """
    Calculate the number of sheets needed for a booklet.

    Returns: Number of sheets required
    """
    # Your code here
    pass
```

## Testing Your Implementation

Create some test cases to verify your solution:

```python
# Test 1: Basic 8-page booklet
booklet_pages(8)
# Expected: [8, 1, 2, 7, 6, 3, 4, 5]

# Test 2: 14 pages (not divisible by 4)
booklet_pages(14)
# Expected: [None, 1, 2, None, 14, 3, 4, 13, 12, 5, 6, 11, 10, 7, 8, 9]

# Test 3: 4 pages (minimum)
booklet_pages(4)
# Expected: [4, 1, 2, 3]

# Test 4: 1 page
booklet_pages(1)
# Expected: [None, 1, 2, None] (needs blank pages)
```

<details>
<summary><b>Challenge: Back Cover Support</b></summary>

<p>Add a keyword argument `backcover=True` that ensures the back cover prints with the front cover, even when the number of pages is not a multiple of 4. Blank pages are inserted between the last page and the back cover.</p>

<p><strong>Example output:</strong></p>

```python
>>> booklet_pages(14, backcover=True)
[14, 1, 2, None, None, 3, 4, 13, 12, 5, 6, 11, 10, 7, 8, 9]
```

<p>Notice how page 14 (back cover) now prints with page 1 (front cover), and blank pages are inserted differently.</p>

</details>

<details>
<summary><b>Challenge: Signature Support for Long Books</b></summary>

<p>For much longer books (>40 pages), it's not feasible to design booklets this way, as paper is difficult to fold when stacked too thickly.</p>

<p>Books are grouped into folded signatures (4–5 sheets of 16–20 pages). Each signature is like a mini booklet. These signatures are then stitched together to make the book.</p>

<p>Add support for signatures: assuming a signature size of 5 sheets (20 pages), update the function to return a list of lists containing the page order for books with more than 20 pages.</p>

<p><strong>Example:</strong></p>

```python
>>> booklet_pages(45)  # More than 20 pages
[[20, 1, 2, 19, 18, 3, 4, 17, 16, 5, 6, 15, 14, 7, 8, 13, 12, 9, 10, 11],
 [40, 21, 22, 39, 38, 23, 24, 37, 36, 25, 26, 35, 34, 27, 28, 33, 32, 29, 30, 31],
 [None, 41, 42, None, 45, 43, 44, None]]
```

</details>

----------

# Submission

Before submitting your code, run the automated tests on your functions. In the shell, type `python test_main.py` and press enter to see the results of the testing.
