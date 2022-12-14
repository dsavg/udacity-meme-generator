"""Command-Line Interface tool to generate memes.

usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]

Generate a meme from an image file and some quote

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      path to an image file
  --body BODY      quote body to add to the image
  --author AUTHOR  quote author to add to the image
"""
import os
import random
import argparse
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, _, files in os.walk(images):
            imgs = [os.path.join(root, name)
                    for name in files
                    if '.DS_Store' not in name]

        img = random.choice(imgs)
    else:
        if path.split('.')[-1] != 'jpg':
            raise Exception(f'Unsupported file type inserted. '
                            f'Expecting .jpg, .{path.split(".")[-1]} found')
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate a meme from an '
                                                 'image file and quote')
    parser.add_argument('--path', type=str, default=None,
                        help='path to an image file')
    parser.add_argument('--body', type=str, default=None,
                        help='quote body to add to the image')
    parser.add_argument('--author', type=str, default=None,
                        help='quote author to add to the image')

    args = parser.parse_args()
    print('Meme is available in:',
          generate_meme(args.path, args.body, args.author))
