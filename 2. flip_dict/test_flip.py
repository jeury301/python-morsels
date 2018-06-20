from collections import defaultdict, OrderedDict
import unittest

from flip import flip_dict_of_lists


class FlipDictOfListsTest(unittest.TestCase):

    """Test for flip_dict_of_lists."""

    def test_flip_dict_of_lists(self):
        restaurants_by_people = {
            'Diane': ['Punjabi Tandoor', 'Opera'],
            'Peter': ['Opera', 'Habaneros'],
            'Trey': ['Habaneros', 'Opera', 'Punjabi Tandoor'],
        }
        favorite_restaurants = flip_dict_of_lists(restaurants_by_people)
        favorite_restaurants = {
            k: sorted(v)
            for k, v in favorite_restaurants.items()
        }
        self.assertEqual(favorite_restaurants, {
            'Opera': ['Diane', 'Peter', 'Trey'],
            'Habaneros': ['Peter', 'Trey'],
            'Punjabi Tandoor': ['Diane', 'Trey'],
        })

    def test_works_with_other_dict_types(self):
        dictionary = defaultdict(list)
        dictionary[1].append('a')
        dictionary[2] += ['a', 'b']
        dictionary[3] = ['b', 'c']
        flipped = flip_dict_of_lists(dictionary)
        self.assertEqual(flipped, {
            'a': [1, 2],
            'b': [2, 3],
            'c': [3],
        })

    def test_original_key_order_ordered_maintained(self):
        dictionary = OrderedDict([
            (1, ['a']),
            (2, ['a', 'b']),
            (3, ['b', 'c']),
        ])
        flipped = flip_dict_of_lists(dictionary)
        self.assertEqual(flipped, {
            'a': [1, 2],
            'b': [2, 3],
            'c': [3],
        })

    # To test the Bonus part of this exercise, comment out the following line
    #@unittest.expectedFailure
    def test_custom_dict_type(self):
        dictionary = {'a': [1, 2], 'b': [2, 3]}
        dict_type = OrderedDict
        flipped = flip_dict_of_lists(dictionary, dict_type=dict_type)
        self.assertEqual(flipped, {
            1: ['a'],
            2: ['a', 'b'],
            3: ['b'],
        })
        self.assertEqual(type(flipped), dict_type)

    # To test the Bonus part of this exercise, comment out the following line
    #@unittest.expectedFailure
    def test_key_function(self):
        dictionary = {
            1: ['a'],
            2: ['A', 'b'],
            3: ['B'],
        }
        def normalize(string): return string.upper()
        flipped = flip_dict_of_lists(dictionary, key_func=normalize)
        self.assertEqual(flipped, {
            'A': [1, 2],
            'B': [2, 3],
        })


if __name__ == "__main__":
    unittest.main()