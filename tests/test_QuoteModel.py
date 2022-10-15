"""Check that an `QuoteModel` can be constructed and responds to inspect queries.

To run these tests from the project root, run:

    $ python3 -m unittest --verbose tests.test_QuoteModel
"""


import unittest
from QuoteEngine import QuoteModel

class TestQuoteModel(unittest.TestCase):

    def test_empty_meme(self):
        # empty input is not allowed
        with self.assertRaises(Exception):
            QuoteModel()

    def test_repr(self):
        body = 'Bark'
        author = 'Barker'
        quote = QuoteModel(body, author)
        self.assertEqual(str(quote), f'"{body}" - {author}')

if __name__ == '__main__':
    unittest.main()
