from textwrap import dedent
import unittest

from matrix import matrix_from_string


class MatrixFromStringTests(unittest.TestCase):

    """Tests for matrix_from_string."""

    def test_empty(self):
        self.assertEqual(matrix_from_string(""), [])

    def test_single_item(self):
        self.assertEqual(matrix_from_string("-5"), [[-5]])

    def test_floating_point_numbers(self):
        self.assertEqual(matrix_from_string("8.5\n7.6"), [[8.5], [7.6]])

    def test_two_by_two_matrix(self):
        matrix = matrix_from_string("1 2\n10 20")
        self.assertEqual([[1, 2], [10, 20]], matrix)

    def test_three_by_two_matrix(self):
        matrix = matrix_from_string("9 8 7\n19 18 17")
        self.assertEqual([[9, 8, 7], [19, 18, 17]], matrix)

    def test_extra_newline(self):
        matrix = matrix_from_string("9 8 7\n19 18 17\n")
        self.assertEqual([[9, 8, 7], [19, 18, 17]], matrix)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_lots_of_space(self):
        expected = [
            [ 1,  5,  8, 10],
            [11,  2,  6,  9],
            [14, 12,  3,  7],
            [16, 15, 13,  4],
        ]
        matrix = matrix_from_string(dedent("""
             1  5  8 10

            11  2  6  9

            14 12  3  7

            16 15 13  4
        """))
        self.assertEqual(expected, matrix)
        self.assertEqual(matrix_from_string("1  5\n  \n \n3 4"), [[1, 5], [3, 4]])


if __name__ == "__main__":
    unittest.main()