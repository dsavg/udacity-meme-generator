"""Check that an `Ingestor` can be constructed and responds to inspect queries.

To run these tests from the project root, run:

    $ python3 -m unittest --verbose tests.test_Ingestor
"""

import unittest
from QuoteEngine import Ingestor

class TestIngestor(unittest.TestCase):

    def test_empty_parse(self):
        # empty input is not allowed
        with self.assertRaises(Exception):
            Ingestor.parse()

    def test_parse_text(self):
        path = './_data/DogQuotes/DogQuotesTXT.txt'
        self.assertEqual(str(Ingestor.parse(path)), '["To bork or not to bork" - Bork, '
                                                    '"He who smelt it..." - Stinky]')

    def test_parse_docx(self):
        path = './_data/DogQuotes/DogQuotesDOCX.docx'
        self.assertEqual(str(Ingestor.parse(path)), '["Bark like no one’s listening" - Rex, "RAWRGWAWGGR" - Chewy, '
                                                    '"Life is like peanut butter: crunchy" - Peanut, '
                                                    '"Channel your inner husky" - Tiny]')

    def test_parse_pdf(self):
        path = './_data/DogQuotes/DogQuotesPDF.pdf'
        self.assertEqual(str(Ingestor.parse(path)), """["Treat yo self" - Fluffles, """
                                                    """"Life is like a box of treats" - Forrest Pup, """
                                                    """"It's the size of the fight in the dog" - Bark Twain]""")

    def test_parse_csv(self):
        path = './_data/DogQuotes/DogQuotesCSV.csv'
        self.assertEqual(str(Ingestor.parse(path)), '["Chase the mailman" - Skittle, '
                                                    '"When in doubt, go shoe-shopping" - Mr. Paws]')

    def test_parse_py(self):
        # only .txt, .docx, .pdf, .csv files allowed
        path = './_data/DogQuotes/NotAcceptedFileFormat.py'
        with self.assertRaises(Exception):
            self.assertIsNone(Ingestor.parse(path))


if __name__ == '__main__':
    unittest.main()
