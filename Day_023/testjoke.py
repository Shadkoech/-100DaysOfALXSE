#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
from joke import len_joke, get_joke


class TestJoke(unittest.TestCase):

    @patch('joke.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'Why was the math book sad? Because it had too many problems.'
        # The length of the joke above is 58
        self.assertEqual(len_joke(), 60)

    @patch('joke.requests.get')
    def test_get_joke(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'setup': 'Why was the math book sad?', 'punchline': 'Because it had too many problems.'}

        mock_requests.return_value = mock_response

        self.assertEqual(get_joke(), 'Why was the math book sad?\nBecause it had too many problems.')


if __name__ == '__main__':
    unittest.main()

