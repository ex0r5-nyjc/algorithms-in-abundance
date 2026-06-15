import unittest
import tempfile
import os

from main import (
    simple_diff,
    count_lines_by_status,
    apply_diff,
    find_common_lines,
    reverse_diff,
    texts_are_identical
)


class TestSimpleDiff(unittest.TestCase):

    def test_simple_diff_identical_texts(self):
        """Test diff of identical texts"""
        text1 = "Hello world\nLine 2\nLine 3"
        text2 = "Hello world\nLine 2\nLine 3"

        result = simple_diff(text1, text2)

        # Should contain only unchanged lines
        self.assertIn('  Hello world', result)
        self.assertIn('  Line 2', result)
        self.assertIn('  Line 3', result)
        self.assertNotIn('-', result)
        self.assertNotIn('+', result)

    def test_simple_diff_completely_different(self):
        """Test diff of completely different texts"""
        text1 = "Line 1\nLine 2\nLine 3"
        text2 = "A\nB\nC"

        result = simple_diff(text1, text2)

        # Should show deletions and additions
        self.assertIn('- Line 1', result)
        self.assertIn('- Line 2', result)
        self.assertIn('- Line 3', result)
        self.assertIn('+ A', result)
        self.assertIn('+ B', result)
        self.assertIn('+ C', result)

    def test_simple_diff_with_addition(self):
        """Test diff where text2 has additions"""
        text1 = "Hello world\nGoodbye"
        text2 = "Hello world\nNew line\nGoodbye"

        result = simple_diff(text1, text2)

        # Should show unchanged lines with addition
        self.assertIn('  Hello world', result)
        self.assertIn('  Goodbye', result)
        self.assertIn('+ New line', result)

    def test_simple_diff_with_deletion(self):
        """Test diff where text2 has deletions"""
        text1 = "Hello world\nRemove this\nGoodbye"
        text2 = "Hello world\nGoodbye"

        result = simple_diff(text1, text2)

        # Should show deletion
        self.assertIn('  Hello world', result)
        self.assertIn('  Goodbye', result)
        self.assertIn('- Remove this', result)

    def test_simple_diff_with_modification(self):
        """Test diff where text2 has modifications"""
        text1 = "Hello world\nOld text\nGoodbye"
        text2 = "Hello world\nNew text\nGoodbye"

        result = simple_diff(text1, text2)

        # Should show deletion and addition
        self.assertIn('- Old text', result)
        self.assertIn('+ New text', result)

    def test_simple_diff_empty_texts(self):
        """Test diff with empty texts"""
        # Both empty
        result1 = simple_diff("", "")
        self.assertEqual(result1, "")

        # One empty
        result2 = simple_diff("", "Some text")
        self.assertIn('+ Some text', result2)

        # Other empty
        result3 = simple_diff("Some text", "")
        self.assertIn('- Some text', result3)

    def test_count_lines_by_status_basic(self):
        """Test counting lines by status"""
        text1 = "Hello\nRemove\nKeep"
        text2 = "Hello\nAdd\nKeep"

        diff_result = simple_diff(text1, text2)
        counts = count_lines_by_status(diff_result)

        self.assertEqual(counts['same'], 2)  # "Hello", "Keep"
        self.assertEqual(counts['removed'], 1)  # "Remove"
        self.assertEqual(counts['added'], 1)  # "Add"

    def test_count_lines_by_status_no_changes(self):
        """Test counting when there are no changes"""
        text1 = "Hello\nWorld"
        text2 = "Hello\nWorld"

        diff_result = simple_diff(text1, text2)
        counts = count_lines_by_status(diff_result)

        self.assertEqual(counts['same'], 2)
        self.assertEqual(counts['removed'], 0)
        self.assertEqual(counts['added'], 0)

    def test_apply_diff_basic(self):
        """Test applying a diff"""
        original = "Hello world\nOld text\nGoodbye"
        modified = "Hello world\nNew text\nGoodbye"

        diff_result = simple_diff(original, modified)
        result = apply_diff(original, diff_result)

        # Result should match the modified text
        self.assertEqual(result, modified)

    def test_apply_diff_no_changes(self):
        """Test applying diff with no changes"""
        original = "Hello world\nGoodbye"
        diff_result = simple_diff(original, original)

        result = apply_diff(original, diff_result)

        # Result should be unchanged
        self.assertEqual(result, original)

    def test_find_common_lines_basic(self):
        """Test finding common lines"""
        text1 = "A\nB\nC\nD"
        text2 = "C\nA\nE\nB"

        result = find_common_lines(text1, text2)

        # Common lines in order from text1: A, B, C
        self.assertIn('A', result)
        self.assertIn('B', result)
        self.assertIn('C', result)
        self.assertNotIn('D', result)
        self.assertNotIn('E', result)

    def test_find_common_lines_no_common(self):
        """Test when there are no common lines"""
        text1 = "A\nB\nC"
        text2 = "X\nY\nZ"

        result = find_common_lines(text1, text2)
        self.assertEqual(result, [])

    def test_find_common_lines_identical(self):
        """Test when texts are identical"""
        text1 = "A\nB\nC"
        text2 = "A\nB\nC"

        result = find_common_lines(text1, text2)
        self.assertEqual(result, ['A', 'B', 'C'])

    def test_reverse_diff_basic(self):
        """Test reversing a diff"""
        text1 = "Hello world\nOld text\nGoodbye"
        text2 = "Hello world\nNew text\nGoodbye"

        diff_result = simple_diff(text1, text2)
        reversed_result = reverse_diff(diff_result)

        # Should swap + and -
        self.assertIn('+ Old text', reversed_result)
        self.assertIn('- New text', reversed_result)

    def test_texts_are_identical_true(self):
        """Test checking if texts are identical"""
        text1 = "Hello\nWorld"
        text2 = "Hello\nWorld"

        result = texts_are_identical(text1, text2)
        self.assertTrue(result)

    def test_texts_are_identical_false(self):
        """Test checking if texts are different"""
        text1 = "Hello\nWorld"
        text2 = "Hello\nUniverse"

        result = texts_are_identical(text1, text2)
        self.assertFalse(result)

    def test_simple_diff_preserves_line_order(self):
        """Test that diff preserves line order"""
        text1 = "Line 1\nLine 2\nLine 3"
        text2 = "Line 1\nModified\nLine 3"

        result = simple_diff(text1, text2)

        # Check that lines appear in correct order
        lines = result.split('\n')
        line1_idx = next(i for i, line in enumerate(lines) if 'Line 1' in line)
        modified_idx = next(i for i, line in enumerate(lines) if 'Modified' in line)
        line3_idx = next(i for i, line in enumerate(lines) if 'Line 3' in line)

        self.assertLess(line1_idx, modified_idx)
        self.assertLess(modified_idx, line3_idx)

    def test_output_format_consistency(self):
        """Test that diff output has consistent format"""
        test_cases = [
            ("Hello\nWorld", "Hello\nWorld"),
            ("Line 1\nLine 2", "Modified 1\nModified 2"),
            ("", "Some text"),
            ("Some text", ""),
        ]

        for text1, text2 in test_cases:
            result = simple_diff(text1, text2)

            # Result should always be a string
            assert isinstance(result, str), "Diff result should be a string"

    def test_no_change_consistency(self):
        """Test that applying diff with no changes preserves original"""
        test_texts = [
            "Hello\nWorld",
            "Single line",
            "",
            "Multi\nline\ntext"
        ]

        for text in test_texts:
            diff_result = simple_diff(text, text)
            result = apply_diff(text, diff_result)

            # Applying a no-change diff should return original
            assert result == text, "No-change diff should preserve original"

    def test_common_is_subset(self):
        """Test that common lines are subset of both texts"""
        text1 = "A\nB\nC\nD"
        text2 = "C\nA\nE\nB"

        common = find_common_lines(text1, text2)

        # All common lines should appear in text1
        lines1 = set(text1.split('\n'))
        for line in common:
            assert line in lines1, f"Common line {line} should be in text1"

    def test_identical_texts_property(self):
        """Test that identical texts return True"""
        test_texts = [
            "Hello\nWorld",
            "Single line",
            "",
            "Multi\nline\ntext"
        ]

        for text in test_texts:
            result = texts_are_identical(text, text)
            assert result == True, "Text should be identical to itself"


if __name__ == '__main__':
    unittest.main()
