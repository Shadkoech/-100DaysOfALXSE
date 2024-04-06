#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from joke import len_joke


class TestJoke(unittest.TestCase):

    # we want to mock the get_joke function since it depends on
    # factors such as internet connection to execute

    @patch('joke.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'one'
        # we have mocked whatever joke would be returned to 'one' and
        # its length is 3
        self.assertEqual(len_joke(), 3)

if __name__ == '__main__':
    unittest.main()