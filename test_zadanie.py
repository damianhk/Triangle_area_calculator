import unittest
import io
import sys
from zadanie import trianagle_area, read_data


class TestReadData(unittest.TestCase):
    def test_values_correct(self):
        # Test data convertion
        sys.stdin = io.StringIO('1')
        self.assertEqual(read_data(), [1.0])

        sys.stdin = io.StringIO('20')
        self.assertEqual(read_data(), [20.0])

        sys.stdin = io.StringIO('-5')
        self.assertEqual(read_data(), [-5.0])

        sys.stdin = io.StringIO('-5.0')
        self.assertEqual(read_data(), [-5.0])

        sys.stdin = io.StringIO('1 3 6\n')
        self.assertEqual(read_data(), [1, 3, 6])

        sys.stdin = io.StringIO('''4 5 6
                                    Lorem ipsum dolor sit amet,
                                    consectetur adipiscing elit.
                                    Phasellus nec fermentum massa.
                                    ''')
        self.assertEqual(read_data(), [4, 5, 6])

    def test_values_not_correct(self):
        # Make sure value errors are raised when necessary
        sys.stdin = io.StringIO('1s')
        self.assertRaises(ValueError, read_data)

        sys.stdin = io.StringIO('text')
        self.assertRaises(ValueError, read_data)

        sys.stdin = io.StringIO('')
        self.assertRaises(ValueError, read_data)


class TestTrianagleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when sides > 0
        self.assertAlmostEqual(trianagle_area([2, 3, 4]), 2.90)
        self.assertAlmostEqual(trianagle_area((2, 3, 4)), 2.90)
        self.assertAlmostEqual(trianagle_area({2, 3, 4}), 2.90)
        self.assertAlmostEqual(trianagle_area([3.4, 5.6, 7.8]), 8.4)

    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, trianagle_area, [-2, 3, 4])
        self.assertRaises(ValueError, trianagle_area, [2, 3, 4, 5])
        self.assertRaises(ValueError, trianagle_area, [2, 5])
        self.assertRaises(ValueError, trianagle_area, [1, 1, 2])
        self.assertRaises(ValueError, trianagle_area, [1, 1, 5])

    def test_types(self):
        # Make sure type errors are raised when necessary
        self.assertRaises(TypeError, trianagle_area, [3+5j, 2, 4])
        self.assertRaises(TypeError, trianagle_area, [True, 1, 2])
        self.assertRaises(TypeError, trianagle_area, ['text', 2, 4])
        self.assertRaises(TypeError, trianagle_area, [[1], 2, 4])
        self.assertRaises(TypeError, trianagle_area, [{'key': 1}, 2, 4])
        self.assertRaises(TypeError, trianagle_area, [{1, 3}, 2, 4])


if __name__ == '__main__':
    unittest.main()
