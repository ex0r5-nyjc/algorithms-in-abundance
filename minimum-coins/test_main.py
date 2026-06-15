import unittest

from main import (
    get_change,
    get_change_limited,
    get_change_recursive,
    count_coins,
    validate_change
)


class TestMinimumCoins(unittest.TestCase):

    def setUp(self):
        """Standard denomination set for testing"""
        self.standard_denomination = (1.00, 0.50, 0.20, 0.10, 0.05, 0.01)

    def test_get_change_basic_case(self):
        """Test basic change calculation"""
        result = get_change(0.90, self.standard_denomination)
        expected = [0.50, 0.20, 0.20]

        self.assertEqual(result, expected, f'Expected {expected}, got {result}')

    def test_get_change_exact_denomination(self):
        """Test when value exactly matches a denomination"""
        result = get_change(0.50, self.standard_denomination)
        expected = [0.50]

        self.assertEqual(result, expected, f'Expected {expected}, got {result}')

    def test_get_change_small_amount(self):
        """Test change for small amounts"""
        result = get_change(0.01, self.standard_denomination)
        expected = [0.01]

        self.assertEqual(result, expected, f'Expected {expected}, got {result}')

    def test_get_change_multiple_same_coins(self):
        """Test when multiple coins of same denomination are needed"""
        result = get_change(0.40, self.standard_denomination)
        expected = [0.20, 0.20]

        self.assertEqual(result, expected, f'Expected {expected}, got {result}')

    def test_get_change_complex_amount(self):
        """Test change for a complex amount"""
        result = get_change(1.37, self.standard_denomination)

        # Validate the result sums correctly
        total = sum(result)
        self.assertAlmostEqual(total, 1.37, places=2,
                             msg=f'Sum of coins {result} should equal 1.37')

    def test_get_change_zero_amount(self):
        """Test change for zero amount"""
        result = get_change(0.00, self.standard_denomination)
        expected = []

        self.assertEqual(result, expected, f'Expected {expected}, got {result}')

    def test_get_change_limited_basic_case(self):
        """Test limited coins with the example from README"""
        available_coins = [1.00, 0.20, 0.20, 0.20, 0.20, 0.20, 0.10, 0.10]
        result = get_change_limited(0.90, available_coins)
        expected = [0.20, 0.20, 0.20, 0.20, 0.10]

        self.assertEqual(result, expected, f'Expected {expected}, got {result}')

    def test_get_change_limited_insufficient_coins(self):
        """Test when available coins are insufficient"""
        available_coins = [0.10, 0.10]  # Only 0.20 available
        result = get_change_limited(0.50, available_coins)

        # Should return what's available or indicate insufficiency
        total = sum(result) if result else 0
        self.assertLessEqual(total, 0.50, 'Should not exceed available amount')

    def test_get_change_recursive_integer_amounts(self):
        """Test recursive approach with integer amounts (cents)"""
        denominations = (100, 50, 25, 10, 5, 1)  # Standard US coins in cents
        result = get_change_recursive(90, denominations)

        # Should use 50 + 25 + 10 + 5 = 90 cents
        total = sum(result)
        self.assertEqual(total, 90, f'Sum should be 90, got {total}')

    def test_get_change_recursive_multiple_solutions(self):
        """Test that recursive approach finds a valid solution"""
        denominations = (100, 50, 25, 10, 5, 1)
        result = get_change_recursive(67, denominations)

        # Validate the result
        total = sum(result)
        self.assertEqual(total, 67, f'Sum should be 67, got {total}')

    def test_count_coins_basic(self):
        """Test counting coins by denomination"""
        coins = [0.50, 0.20, 0.20, 0.10]
        result = count_coins(coins)

        expected_counts = {
            0.50: 1,
            0.20: 2,
            0.10: 1
        }

        self.assertEqual(result, expected_counts, f'Expected {expected_counts}, got {result}')

    def test_count_coins_empty_list(self):
        """Test counting empty list of coins"""
        result = count_coins([])
        expected = {}

        self.assertEqual(result, expected, f'Expected {expected}, got {result}')

    def test_validate_change_correct_amount(self):
        """Test validation of correct change"""
        coins = [0.50, 0.20, 0.20]
        target = 0.90

        result = validate_change(coins, target)
        self.assertTrue(result, 'Change should be valid')

    def test_validate_change_incorrect_amount(self):
        """Test validation of incorrect change"""
        coins = [0.50, 0.20, 0.10]  # Sum is 0.80
        target = 0.90

        result = validate_change(coins, target)
        self.assertFalse(result, 'Change should be invalid')

    def test_validate_change_empty_list(self):
        """Test validation of empty change list"""
        coins = []
        target = 0.00

        result = validate_change(coins, target)
        self.assertTrue(result, 'Empty change should be valid for zero target')

    def test_get_change_result_sums_correctly(self):
        """Test that change always sums to target value"""
        test_cases = [
            (0.10, self.standard_denomination),
            (0.25, self.standard_denomination),
            (0.99, self.standard_denomination),
            (1.50, self.standard_denomination)
        ]

        for value, denomination in test_cases:
            result = get_change(value, denomination)
            total = sum(result)

            # Allow small floating point errors
            self.assertAlmostEqual(total, value, places=2,
                                 msg=f'Sum of {result} should equal {value}')

    def test_validate_change_correctness(self):
        """Test validation logic"""
        # Correct change should validate
        coins = [0.50, 0.20, 0.20]
        target = 0.90
        result = validate_change(coins, target)
        actual_sum = round(sum(coins), 2)

        self.assertTrue(result)
        self.assertEqual(actual_sum, target)

        # Incorrect change should not validate
        coins = [0.50, 0.20, 0.10]
        target = 0.90
        result = validate_change(coins, target)
        actual_sum = round(sum(coins), 2)

        self.assertFalse(result)
        self.assertNotEqual(actual_sum, target)

    def test_count_coins_preserves_total(self):
        """Test that counting coins doesn't lose information"""
        coins = [0.50, 0.20, 0.20, 0.10]
        counts = count_coins(coins)

        # Reconstruct the coins from counts
        reconstructed = []
        for denomination, count in counts.items():
            reconstructed.extend([denomination] * count)

        # Sums should be equal
        self.assertEqual(sum(coins), sum(reconstructed),
                       msg='Counting and reconstructing should preserve total value')


if __name__ == '__main__':
    unittest.main()
