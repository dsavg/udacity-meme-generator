"""Check that an `MemeEngine` can be constructed and responds to inspect queries.

To run these tests from the project root, run:

    $ python3 -m unittest --verbose tests.test_test_MemeEngine
"""

import unittest
from MemeEngine import *

class TestMemeEngine(unittest.TestCase):

    def test_empty_meme(self):
        meme = MemeEngine()
        self.assertEqual(str(meme), 'MemeEngine(output_dir="./tmp")')
        self.assertIsNone(meme.img_path)
        self.assertIsNone(meme.body)
        self.assertIsNone(meme.author)

    def test_repr(self):
        meme = MemeEngine('./tmp')
        self.assertEqual(str(meme), 'MemeEngine(output_dir="./tmp")')

    def test_make_meme(self):
        meme = MemeEngine('./tmp')
        t_img = "./_data/photos/dog/pumbaa_1.jpg"
        t_body = "Bark"
        t_author = "Pumbaa"

        # raise error if no arguments passed in make_meme method
        with self.assertRaises(Exception):
            meme.make_meme()

        self.assertIsNone(meme.img_path)
        self.assertIsNone(meme.body)
        self.assertIsNone(meme.author)

        path = meme.make_meme(t_img, t_body, t_author)
        self.assertEqual(str(meme), 'MemeEngine(output_dir="./tmp")')
        self.assertEqual(str(meme._message),f'"{t_body}" \n- {t_author}')
        self.assertEqual(meme.body, t_body)
        self.assertEqual(meme.author, t_author)

if __name__ == '__main__':
    unittest.main()
