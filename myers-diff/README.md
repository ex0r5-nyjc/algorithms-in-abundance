# Objective

This assignment is a stretch task: do not attempt this until you have completed the other two.

Your task is to implement a function that compares two multi-line strings and returns the differences in a standard format, known as a **diff**.

----------

# Simple Text Comparison: Finding Differences Between Two Texts

We often need to compare two things to see what has changed or is different between them. Text comparison is used in:
- Document comparison (seeing what changed between drafts)
- Version control systems (comparing file versions)
- Collaboration tools (showing edits and suggestions)

## Task: Compare Two Texts Line by Line

Write a function `simple_diff(text1: str, text2: str) -> str` that compares two texts and shows the differences.

### What You Need to Do

Your function should:
1. Split both texts into lines
2. Compare the texts line by line
3. Show which lines are the same, which were removed, and which were added
4. Return a formatted string showing the differences

### Expected Output Format

```
  line that is the same in both (starts with a space)
- line that was removed from text1 (starts with -)
+ line that was added in text2 (starts with +)
```

### Example

```python
text1 = """Hello world
This is line 2
Goodbye"""

text2 = """Hello world
This is modified
Goodbye
New line"""

result = simple_diff(text1, text2)
print(result)
```

Expected output:
```
  Hello world
- This is line 2
+ This is modified
  Goodbye
+ New line
```

## Step-by-Step Algorithm

Here's a clear approach to solve this problem:

1. **Split both texts into lines**
   - Use an appropriate method to obtain contents of both files as lists of lines

2. **Handle different length texts**
   - Find which text is longer
   - Compare up to the length of the shorter text first

3. **Compare line by line**
   - For each position, check if the lines are equal
   - If equal: mark with `  ` (two spaces)
   - If different: mark old line with `-` and new line with `+`

4. **Handle extra lines**
   - If text1 is longer, remaining lines are deletions (`-`)
   - If text2 is longer, remaining lines are additions (`+`)

5. **Build the result string**
   - Format each line with the appropriate marker
   - Join all lines with newline characters

## Implementation Hints

```python
def simple_diff(text1: str, text2: str) -> str:
    # Step 1: Split into lines
    lines1 = text1.split('\n')
    lines2 = text2.split('\n')

    # Step 2: Find the maximum length
    max_length = max(len(lines1), len(lines2))

    result = []

    # Step 3: Compare line by line
    for i in range(max_length):
        # Handle case where one text is shorter
        if i >= len(lines1):
            # Only in text2 (addition)
            result.append(f"+ {lines2[i]}")
        elif i >= len(lines2):
            # Only in text1 (deletion)
            result.append(f"- {lines1[i]}")
        elif lines1[i] == lines2[i]:
            # Same in both
            result.append(f"  {lines1[i]}")
        else:
            # Different
            result.append(f"- {lines1[i]}")
            result.append(f"+ {lines2[i]}")

    # Step 4: Join with newlines
    return '\n'.join(result)
```

## Additional Functions to Implement

### Function 1: count_lines_by_status(diff_output: str) -> dict

Count how many lines fall into each category (same, removed, added).

```python
def count_lines_by_status(diff_output: str) -> dict:
    """
    Count lines by their status in the diff output.

    Returns: {'same': count, 'removed': count, 'added': count}
    """
    # Your code here
```

### Function 2: apply_diff(original_text: str, diff_output: str) -> str

Apply a diff output to transform original text into the modified version.

```python
def apply_diff(original_text: str, diff_output: str) -> str:
    """
    Apply the diff output to original text to get the modified version.

    For this simplified version, you can:
    1. Parse the diff output
    2. Keep lines marked with '  ' or '+'
    3. Skip lines marked with '-'
    4. Return the reconstructed text
    """
    # Your code here
```

## Testing Your Implementation

Create some test cases to verify your solution:

```python
# Test 1: Identical texts
text1 = "Hello\nWorld"
text2 = "Hello\nWorld"
# Expected: only '  ' markers

# Test 2: Completely different
text1 = "A\nB\nC"
text2 = "X\nY\nZ"
# Expected: alternating '-' and '+' markers

# Test 3: Text2 is longer
text1 = "Hello"
text2 = "Hello\nWorld"
# Expected: one '+' marker

# Test 4: Text1 is longer
text1 = "Hello\nWorld"
text2 = "Hello"
# Expected: one '-' marker
```

<details>
<summary><b>Challenge: Find Common Lines</b></summary>
<p>Write a function `find_common_lines(text1: str, text2: str) -> list` that returns a list of lines that appear in both texts, in the order they appear in text1.</p>

<p>This is a simplified version of finding the "longest common subsequence" - a concept used in more advanced diff algorithms.</p>
</details>

<details>
<summary><b>Challenge: Reverse Diff</b></summary>
<p>Write a function `reverse_diff(diff_output: str) -> str` that swaps the '+' and '-' markers. This would transform a diff that shows how to get from A→B into a diff that shows how to get from B→A.</p>
</details>

----------

# Submission

Before submitting your code, run the automated tests on your functions. In the shell, type `python test_main.py` and press enter to see the results of the testing.
