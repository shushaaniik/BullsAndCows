import unittest
from unittest import mock
from src.utils.work_with_codes import check_code, get_bulls_cows,\
                                      generate_all_codes


class CheckCodeTest(unittest.TestCase):
    def test_check_code_wrong_length(self):
        code = "12345"
        length = 4
        self.assertFalse(check_code(code, length))

    def test_check_code_containing_not_digits(self):
        code = "1y76"
        length = 4
        self.assertFalse(check_code(code, length))

    def test_check_code_containing_repetition(self):
        code = "123453"
        length = 4
        self.assertFalse(check_code(code, length))

    def test_check_valid_code(self):
        code = "1234567"
        length = 7
        self.assertTrue(check_code(code, length))


class GetBullsAndCowsTest(unittest.TestCase):
    def test_get_bulls_cows_called_check_code_false(self):
        guess = "12r4"
        code = "1243"
        length = 4
        with mock.patch('src.utils.work_with_codes.check_code') as mock_check_code:
            mock_check_code.return_value = False
            bulls, cows = get_bulls_cows(guess, code, length)
            mock_check_code.assert_called_once_with(guess, length)
        self.assertEqual(bulls, -1)
        self.assertEqual(cows, -1)

    def test_get_bulls_cows_called_check_code(self):
        guess = "1234"
        code = "1243"
        length = 4
        with mock.patch('src.utils.work_with_codes.check_code') as mock_check_code:
            mock_check_code.return_value = True
            bulls, cows = get_bulls_cows(guess, code, length)
            mock_check_code.assert_called_once_with(guess, length)
        self.assertEqual(bulls, 2)
        self.assertEqual(cows, 2)

    def test_get_bulls_cows_0_bulls_0_cows(self):
        guess = "5678"
        code = "1234"
        bulls, cows = get_bulls_cows(guess, code, 4)
        self.assertEqual(bulls, 0)
        self.assertEqual(cows, 0)

    def test_get_bulls_cows_4_bulls(self):
        guess = "9876"
        code = "9876"
        bulls, cows = get_bulls_cows(guess, code, 4)
        self.assertEqual(bulls, 4)
        self.assertEqual(cows, 0)

    def test_get_bulls_cows_4_cows(self):
        guess = "1234"
        code = "4321"
        bulls, cows = get_bulls_cows(guess, code, 4)
        self.assertEqual(bulls, 0)
        self.assertEqual(cows, 4)


class GenerateAllCodes(unittest.TestCase):
    def test_length_of_all_possible_codes_for_4_length(self):
        self.assertEqual(len(generate_all_codes(4)), 5040)

    def test_length_of_all_possible_codes_for_6_length(self):
        self.assertEqual(len(generate_all_codes(6)), 151200)


if __name__ == '__main__':
    unittest.main()
