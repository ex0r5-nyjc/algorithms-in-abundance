from typing import List, Optional


def booklet_pages(n: int, backcover: bool = False) -> List[Optional[int]]:
    """
    Generate page order for booklet printing.

    Args:
        n: Number of pages in the booklet
        backcover: If True, ensure back cover prints with front cover

    Returns:
        List of page numbers in printing order (None for blank pages)
    """
    # Write your code here
    if n == 0:
        return []
    if n == 1:
        n = 2
    pages = []
    remainder = n % 4
    if remainder != 0:
        remainder = 4 - remainder
    for i in range(1, n + 1):
        pages.append(i)
    for i in range(remainder):
        if backcover:
            pages.insert(-1, None)  # inserts BEFORE index
        else:
            pages.append(None)
    output = []
    npages = n + remainder
    for i in range(0, npages // 2, 2):
        output.append(pages[npages - i - 1])
        output.append(pages[i])
        output.append(pages[i + 1])
        output.append(pages[npages - i - 2])
    return output


def validate_booklet_layout(page_order: List[Optional[int]]) -> bool:
    """
    Validate that a booklet layout will fold correctly.

    Args:
        page_order: List of page numbers in printing order

    Returns:
        True if layout is valid, False otherwise
    """
    # Write your code here
    if len(page_order) % 4 != 0:
        return False
    backcover = False
    front = []
    back = []
    for i in range(0, len(page_order), 4):
        pend, pfirst, psecond, psecondfromend = page_order[i:i+4]
        for page in (pend, pfirst, psecondfromend, psecond):
            if not (type(page) == int or page == None):
                return False
        front.append(pfirst)
        front.append(psecond)
        back.append(pend)
        back.append(psecondfromend)
    if None in back and back[0] != None:
        backcover = True
    else:
        backcover = False
    back.reverse()
    number = 1
    for page in front:
        if page != number:
            return False
        number += 1
    noneyet = False
    for page in back:
        if page != number:
            if page != None:
                return False
            if not noneyet:
                noneyet = True
        elif noneyet:
            return (back.index(page) != len(page_order) - 1)
        else:
            number += 1
    return True

def count_sheets(n: int) -> int:
    """
    Calculate the number of sheets needed for a booklet.

    Args:
        n: Number of pages in the booklet

    Returns:
        Number of sheets required
    """
    # Write your code here
    if n % 4 == 0:
        return n // 4
    return (n // 4) + 1


def booklet_pages_with_signatures(n: int, signature_size: int = 20) -> List[List[Optional[int]]]:
    """
    Generate page order for long books using signatures.

    Args:
        n: Number of pages in the book
        signature_size: Number of pages per signature (default 20)

    Returns:
        List of lists, where each inner list represents a signature's page order
    """
    # Write your code here for the signature challenge
    complete_books = n // signature_size
    rem_pages = n % signature_size
    output = []
    for i in range(complete_books):
        smallbook = booklet_pages(signature_size)
        for j in range(signature_size):
            smallbook[j] += i * signature_size
        output.append(smallbook)
    if rem_pages != 0:
        smallbook = booklet_pages(rem_pages)
        for j in range(rem_pages):
            if smallbook[j] != None:
                smallbook[j] += complete_books * signature_size
        output.append(smallbook)
    return output

def calculate_fold_positions(page_order: List[Optional[int]]) -> List[tuple]:
    """
    Calculate where pages will be positioned when folded.

    Args:
        page_order: List of page numbers in printing order

    Returns:
        List of tuples showing which pages print together on each sheet
    """
    # Write your code here for additional challenge
    output = []
    for i in range(0, len(page_order), 4):
        a, b, c, d = page_order[i:i+4]
        output.append((a, b, c, d))
    return output


def estimate_paper_needed(n: int, signature_size: int = 20) -> dict:
    """
    Estimate paper requirements for a booklet.

    Args:
        n: Number of pages in the booklet
        signature_size: Number of pages per signature

    Returns:
        Dictionary with sheets_needed, total_sheets, waste_pages info
    """
    # Write your code here for additional challenge
    # apparently sheets_needed is the rounded up page number while total_sheets is number of sheets
    rem_pages = n % signature_size
    if rem_pages != 0:
        rem_pages = signature_size - rem_pages
    new_pages = n + rem_pages
    return {"sheets_needed": new_pages, "total_sheets": (new_pages // 4), "waste_pages": rem_pages}

    

if __name__ == "__main__":
    breakpoint()
    for i in range(1, 17):
        print(booklet_pages(i))
        print(booklet_pages(i, backcover=True))
    breakpoint()
    print(booklet_pages_with_signatures(45))
    print(booklet_pages_with_signatures(8))