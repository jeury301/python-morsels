import unittest

from with_previous import with_previous


class WithPreviousTests(unittest.TestCase):

    """Tests for with_previous."""

    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_three(self):
        inputs = [1, 2, 3]
        outputs = [(1, None), (2, 1), (3, 2)]
        self.assertIterableEqual(with_previous(inputs), outputs)

    def test_empty(self):
        self.assertIterableEqual(with_previous([]), [])

    def test_one_item(self):
        self.assertIterableEqual(with_previous([1]), [(1, None)])

    def test_none(self):
        inputs = [None, None]
        outputs = [(None, None), (None, None)]
        self.assertIterableEqual(with_previous(inputs), outputs)

    def test_string(self):
        inputs = "hey"
        outputs = [('h', None), ('e', 'h'), ('y', 'e')]
        self.assertIterableEqual(with_previous(inputs), outputs)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_lazy_iterable(self):
        inputs = (n**2 for n in [1, 2, 3])
        outputs = [(1, None), (4, 1), (9, 4)]
        self.assertIterableEqual(with_previous(inputs), outputs)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_returns_lazy_iterable(self):
        inputs = (n**2 for n in [1, 2, 3])
        iterable = with_previous(inputs)
        self.assertEqual(iter(iterable), iter(iterable))
        self.assertEqual(next(iterable), (1, None))
        self.assertNotEqual(list(inputs), [])

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_fillvalue_as_keyword_argument_only(self):
        """Test can be called with fillvalue (but only as keyword arg)."""
        inputs = [1, 2, 3]
        outputs = [(1, 0), (2, 1), (3, 2)]
        self.assertIterableEqual(with_previous(inputs, fillvalue=0), outputs)
        with self.assertRaises(TypeError):
            with_previous(inputs, 0)


if __name__ == "__main__":
    unittest.main()