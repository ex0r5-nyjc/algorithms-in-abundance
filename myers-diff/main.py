from typing import List, Dict


def simple_diff(text1: str, text2: str) -> str:
    """
    Compare two texts line by line and show differences.

    Args:
        text1: First text string
        text2: Second text string

    Returns:
        A string showing differences with markers:
        - '  ' for lines that are the same
        - '-' for lines removed from text1
        - '+' for lines added in text2
    """
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


def count_lines_by_status(diff_output: str) -> Dict[str, int]:
    """
    Count lines by their status in the diff output.

    Args:
        diff_output: The diff output string from simple_diff

    Returns:
        A dictionary with keys 'same', 'removed', 'added' and their counts
    """
    # Write your code here
    pass


def apply_diff(original_text: str, diff_output: str) -> str:
    """
    Apply the diff output to original text to get the modified version.

    Args:
        original_text: The original text
        diff_output: The diff output from simple_diff

    Returns:
        The modified text after applying the diff
    """
    # Write your code here
    pass


def find_common_lines(text1: str, text2: str) -> List[str]:
    """
    Find lines that appear in both texts.

    Args:
        text1: First text string
        text2: Second text string

    Returns:
        A list of lines that appear in both texts, in order from text1
    """
    # Write your code here
    pass


def reverse_diff(diff_output: str) -> str:
    """
    Reverse a diff by swapping '+' and '-' markers.

    Args:
        diff_output: The diff output to reverse

    Returns:
        The reversed diff output
    """
    # Write your code here
    pass


def texts_are_identical(text1: str, text2: str) -> bool:
    """
    Check if two texts are identical (line by line).

    Args:
        text1: First text string
        text2: Second text string

    Returns:
        True if texts are identical, False otherwise
    """
    # Write your code here
    pass
