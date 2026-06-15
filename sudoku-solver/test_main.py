import unittest
from copy import deepcopy

from main import (
    generate,
    get_unused,
    get_unfilled,
    is_complete,
    is_correct,
    solve
)


class TestSudokuSolver(unittest.TestCase):

    def test_generate_returns_puzzle(self):
        """Test that generate returns a valid puzzle structure"""
        puzzle = generate()

        self.assertIsInstance(puzzle, list)
        self.assertEqual(len(puzzle), 3)

        for row in puzzle:
            self.assertIsInstance(row, list)
            self.assertEqual(len(row), 3)

    def test_generate_has_empty_cells(self):
        """Test that generated puzzle has some empty cells"""
        puzzle = generate()

        # Should have at least one None (empty cell)
        has_empty = any(cell is None for row in puzzle for cell in row)
        self.assertTrue(has_empty, 'Generated puzzle should have empty cells')

    def test_get_unused_returns_list(self):
        """Test that get_unused returns a list"""
        puzzle = generate()
        unused = get_unused(puzzle)

        self.assertIsInstance(unused, list)

    def test_get_unused_correct_numbers(self):
        """Test that get_unused returns correct unused numbers"""
        puzzle = [
            [1, 3, None],
            [None, None, 7],
            [9, None, None]
        ]

        unused = get_unused(puzzle)

        # Used numbers are 1, 3, 7, 9
        # So unused should be [2, 4, 5, 6, 8] (order may vary)
        expected_set = {2, 4, 5, 6, 8}
        actual_set = set(unused)

        self.assertEqual(expected_set, actual_set)

    def test_get_unfilled_returns_list(self):
        """Test that get_unfilled returns a list of coordinates"""
        puzzle = generate()
        unfilled = get_unfilled(puzzle)

        self.assertIsInstance(unfilled, list)

    def test_get_unfilled_correct_coordinates(self):
        """Test that get_unfilled returns correct coordinates"""
        puzzle = [
            [1, 3, None],
            [None, None, 7],
            [9, None, None]
        ]

        unfilled = get_unfilled(puzzle)

        # Should return coordinates of None cells
        expected_coords = {(0, 2), (1, 0), (1, 1), (2, 1), (2, 2)}
        actual_coords = set(unfilled)

        self.assertEqual(expected_coords, actual_coords)

    def test_is_complete_filled_puzzle(self):
        """Test that is_complete returns True for filled puzzle"""
        puzzle = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        result = is_complete(puzzle)
        self.assertTrue(result, 'Filled puzzle should be complete')

    def test_is_complete_incomplete_puzzle(self):
        """Test that is_complete returns False for incomplete puzzle"""
        puzzle = [
            [1, 2, None],
            [4, 5, 6],
            [7, 8, 9]
        ]

        result = is_complete(puzzle)
        self.assertFalse(result, 'Puzzle with None should be incomplete')

    def test_is_correct_correct_puzzle(self):
        """Test that is_correct returns True for correct puzzle"""
        puzzle = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        result = is_correct(puzzle)
        self.assertTrue(result, 'Puzzle with numbers 1-9 should be correct')

    def test_is_correct_incorrect_puzzle(self):
        """Test that is_correct returns False for incorrect puzzle"""
        puzzle = [
            [1, 2, 3],
            [4, 5, 5],  # Duplicate 5
            [7, 8, 9]
        ]

        result = is_correct(puzzle)
        self.assertFalse(result, 'Puzzle with duplicates should be incorrect')

    def test_is_correct_incomplete_puzzle(self):
        """Test that is_correct returns False for incomplete puzzle"""
        puzzle = [
            [1, 2, None],
            [4, 5, 6],
            [7, 8, 9]
        ]

        result = is_correct(puzzle)
        self.assertFalse(result, 'Incomplete puzzle should not be correct')

    def test_solve_returns_solution(self):
        """Test that solve returns a solution for the generated puzzle"""
        puzzle = generate()
        solution = solve(puzzle)

        self.assertIsNotNone(solution, 'Should find a solution')
        self.assertIsInstance(solution, list)

        # Verify the solution is correct and complete
        self.assertTrue(is_complete(solution), 'Solution should be complete')
        self.assertTrue(is_correct(solution), 'Solution should be correct')

    def test_solve_does_not_modify_original(self):
        """Test that solve does not modify the original puzzle"""
        original = generate()
        original_copy = deepcopy(original)

        solution = solve(original)

        # Original should be unchanged
        self.assertEqual(original, original_copy, 'Original puzzle should not be modified')

    def test_solve_returns_none_for_unsolvable(self):
        """Test that solve returns None for unsolvable puzzle"""
        # Create an impossible puzzle (already violates constraints)
        puzzle = [
            [1, 1, None],  # Duplicate 1 in same row
            [2, 2, None],
            [3, 3, None]
        ]

        solution = solve(puzzle)
        self.assertIsNone(solution, 'Impossible puzzle should return None')

    def test_solve_specific_puzzle(self):
        """Test solve with a specific known-solvable puzzle"""
        puzzle = [
            [None, 3, None],
            [None, None, 7],
            [9, None, None]
        ]

        solution = solve(puzzle)

        self.assertIsNotNone(solution, 'Should find a solution')
        self.assertTrue(is_complete(solution), 'Solution should be complete')
        self.assertTrue(is_correct(solution), 'Solution should be correct')

    def test_solve_preserves_pre_filled_values(self):
        """Test that solution preserves the pre-filled values"""
        puzzle = [
            [None, 3, None],
            [None, None, 7],
            [9, None, None]
        ]

        # Remember pre-filled positions and values
        pre_filled = {}
        for i in range(3):
            for j in range(3):
                if puzzle[i][j] is not None:
                    pre_filled[(i, j)] = puzzle[i][j]

        solution = solve(puzzle)

        # Check that pre-filled values are preserved
        for (i, j), value in pre_filled.items():
            self.assertEqual(solution[i][j], value,
                           f'Pre-filled value at ({i},{j}) should be preserved')

    def test_solution_validity(self):
        """Test that solution is always valid when not None"""
        puzzle = generate()
        solution = solve(puzzle)

        if solution is not None:
            # Solution should be complete
            assert is_complete(solution), "Solution should be complete"

            # Solution should be correct
            assert is_correct(solution), "Solution should be correct"

            # Solution should have same structure
            assert isinstance(solution, list), "Solution should be a list"
            assert len(solution) == 3, "Solution should be 3x3"

    def test_preservation_property(self):
        """Test that solve preserves pre-filled values"""
        puzzle = generate()

        # Collect pre-filled values
        pre_filled = {}
        for i in range(3):
            for j in range(3):
                if puzzle[i][j] is not None:
                    pre_filled[(i, j)] = puzzle[i][j]

        solution = solve(puzzle)

        if solution is not None:
            # All pre-filled values should be preserved
            for (i, j), value in pre_filled.items():
                assert solution[i][j] == value, \
                    f"Pre-filled value at ({i},{j}) should be preserved"

    def test_helper_functions_consistency(self):
        """Test that helper functions work consistently"""
        puzzle = generate()
        unused = get_unused(puzzle)
        unfilled = get_unfilled(puzzle)

        # Unused should be a list
        assert isinstance(unused, list), "Unused should be a list"

        # Unfilled should be a list of tuples
        assert isinstance(unfilled, list), "Unfilled should be a list"
        for coord in unfilled:
            assert isinstance(coord, tuple), "Each coordinate should be a tuple"
            assert len(coord) == 2, "Each coordinate should have 2 elements"

        # Number of unfilled cells should match
        actual_unfilled_count = sum(1 for row in puzzle for cell in row if cell is None)
        assert len(unfilled) == actual_unfilled_count, \
            "Unfilled count should match actual None cells"


if __name__ == '__main__':
    unittest.main()
