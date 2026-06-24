from typing import List, Dict


def simple_diff(text1: str, text2: str) -> str: # line 85, 55, 67
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
    # # Step 1: Split into lines
    # lines1 = text1.split('\n')
    # lines2 = text2.split('\n')

    # # Step 2: Find the maximum length
    # max_length = max(len(lines1), len(lines2))

    # result = []

    # # Step 3: Compare line by line
    # for i in range(max_length):
    #     # Handle case where one text is shorter
    #     if i >= len(lines1):
    #         # Only in text2 (addition)
    #         result.append(f"+ {lines2[i]}")
    #     elif i >= len(lines2):
    #         # Only in text1 (deletion)
    #         result.append(f"- {lines1[i]}")
    #     elif lines1[i] == lines2[i]:
    #         # Same in both
    #         result.append(f"  {lines1[i]}")
    #     else:
    #         # Different
    #         result.append(f"- {lines1[i]}")
    #         result.append(f"+ {lines2[i]}")

    # # Step 4: Join with newlines
    # return '\n'.join(result)
    
    common = find_common_lines(text1, text2)
    lines1 = text1.split("\n")
    lines2 = text2.split("\n")
    repeat = {}
    track = {}
    com1 = []
    com2 = []
    add = []
    minus = []

    for line in common:
        count1 = lines1.count(line)
        count2 = lines2.count(line)
        repeat[line] = [count1, count2]
        track[line] = [0, 0]
    
    for i in range(len(lines1)):
        if lines1[i] in common and track[lines1[i]][0] < repeat[lines1[i]][0]:
            com1.append(i)
            track[lines1[i]][0] += 1
        else:
            minus.append(i)
    
    for i in range(len(lines2)):
        if lines2[i] in common and track[lines2[i]][1] < repeat[lines2[i]][1]:
            com2.append(i)
            track[lines2[i]][1] += 1
        else:
            add.append(i)

    for i in range(len(com1)):
        if com1[i] > com2[i]:
            for j in range(com1[i] - com2[i]):
                lines2.insert(com2[i], None)
        elif com1[i] < com2[i]:
            for j in range(com2[i] - com1[i]):
                lines1.insert(com1[i], None)
    
    if len(lines1) > len(lines2):
        for i in range(len(lines1) - len(lines2)):
            lines2.append(None)
    elif len(lines1) < len(lines2):
        for i in range(len(lines2) - len(lines1)):
            lines1.append(None)
    
    output = []
    for i in range(len(lines1)):
        if lines1[i] == lines2[i] and lines1[i] != None and lines1[i] != "":
            output.append("  " + lines1[i])
        elif lines1[i] != lines2[i]:
            if lines1[i] != None:
                output.append("- " + lines1[i])
            if lines2[i] != None:
                output.append("+ " + lines2[i])
    return "\n".join(output)


def count_lines_by_status(diff_output: str) -> Dict[str, int]: # line 103, 115
    """
    Count lines by their status in the diff output.

    Args:
        diff_output: The diff output string from simple_diff

    Returns:
        A dictionary with keys 'same', 'removed', 'added' and their counts
    """
    # Write your code here
    output = {"same": 0, "removed": 0, "added": 0}
    diff_lines = diff_output.split("\n")
    for line in diff_lines:
        if line[0] == " ":
            output["same"] += 1
        elif line[0] == "-":
            output["removed"] += 1
        else:
            output["added"] += 1
    return output


def apply_diff(original_text: str, diff_output: str) -> str: # line 128, 138, 243
    """
    Apply the diff output to original text to get the modified version.

    Args:
        original_text: The original text
        diff_output: The diff output from simple_diff

    Returns:
        The modified text after applying the diff
    """
    # Write your code here
    if diff_output == "":
        return ""
    output = []
    diff_lines = diff_output.split("\n")
    for line in diff_lines:
        if line[0] == " " or line[0] == "+":
            output.append(line[2:])
    return "\n".join(output)


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
    lines1 = text1.split("\n")
    lines2 = text2.split("\n")
    output = []
    repeats = {}
    for line in lines1:
        if line not in repeats.keys():
            repeats[line] = 0
        if repeats[line] < lines2.count(line):
            output.append(line)
            repeats[line] += 1
    return output


def reverse_diff(diff_output: str) -> str:
    """
    Reverse a diff by swapping '+' and '-' markers.

    Args:
        diff_output: The diff output to reverse

    Returns:
        The reversed diff output
    """
    # Write your code here
    diff_lines = diff_output.split("\n")
    output = []
    for line in diff_lines:
        if line[0] == "+":
            rest = line[1:]
            output.append("-" + rest)
        elif line[0] == "-":
            rest = line[1:]
            output.append("+" + rest)
        else:
            output.append(line)
    return "\n".join(output)


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
    lines1 = text1.split("\n")
    lines2 = text2.split("\n")
    if len(lines1) != len(lines2):
        return False
    for i in range(len(lines1)):
        if lines1[i] != lines2[i]:
            return False
    return True

if __name__ == "__main__":
    # Test 1: Identical texts
    text1 = "Hello\nWorld"
    text2 = "Hello\nWorld"
    result = simple_diff(text1, text2)
    print(result)
    print(apply_diff(text1, result))
    # Expected: only '  ' markers

    # Test 2: Completely different
    text1 = "A\nB\nC"
    text2 = "X\nY\nZ"
    print(simple_diff(text1, text2))
    # Expected: alternating '-' and '+' markers

    # Test 3: Text2 is longer
    text1 = "Hello"
    text2 = "Hello\nWorld"
    print(simple_diff(text1, text2))
    # Expected: one '+' marker

    # Test 4: Text1 is longer
    text1 = "Hello\nWorld"
    text2 = "Hello"
    print(simple_diff(text1, text2))
    # Expected: one '-' marker

    # Test 5
    text1 = "Hello\nWorld"
    text2 = "Hello\nMy\nWorld"
    result = simple_diff(text1, text2)
    print(result)
    print(count_lines_by_status(result))
    # Expected: one '+' marker

    # Test 6:
    text1 = ""
    text2 = ""
    print(simple_diff(text1, text2))
    # Expected: nothing