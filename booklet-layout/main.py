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
    pass


def validate_booklet_layout(page_order: List[Optional[int]]) -> bool:
    """
    Validate that a booklet layout will fold correctly.

    Args:
        page_order: List of page numbers in printing order

    Returns:
        True if layout is valid, False otherwise
    """
    # Write your code here
    pass


def count_sheets(n: int) -> int:
    """
    Calculate the number of sheets needed for a booklet.

    Args:
        n: Number of pages in the booklet

    Returns:
        Number of sheets required
    """
    # Write your code here
    pass


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
    pass


def calculate_fold_positions(page_order: List[Optional[int]]) -> List[tuple]:
    """
    Calculate where pages will be positioned when folded.

    Args:
        page_order: List of page numbers in printing order

    Returns:
        List of tuples showing which pages print together on each sheet
    """
    # Write your code here for additional challenge
    pass


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
    pass
