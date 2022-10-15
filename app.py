"""Flask app.

To run:
$ export FLASK_APP=app.py
$ flask run --host 0.0.0.0 --port 3000 --reload
"""
import os
import random
import itertools
import requests
from flask import Flask, render_template, request

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes_list = [Ingestor.parse(q) for q in quote_files]
    # Flatten the list of lists
    _quotes = list(itertools.chain(*quotes_list))

    images_path = "./_data/photos/dog/"

    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    _imgs = [images_path + f for f in os.listdir(images_path)]

    return _quotes, _imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme.

    Use the random python standard library class to:
    1. select a random image from imgs array
    2. select a random quote from the quotes array
    """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    print(img, quote)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    temp_img = f'{random.randint(1, 100000)}.jpg'

    # Use requests to get the image_url, body, and author
    # from the form params
    img = request.form.get("image_url")
    body = request.form.get("body")
    author = request.form.get("author")

    # save the image to a temporary location
    img_content = requests.get(img, stream=True, timeout=5).content
    with open(temp_img, 'wb') as f:
        f.write(img_content)

    # Use the meme object to generate a meme using this temp
    # file and the body and author form paramaters.
    path = meme.make_meme(temp_img, body, author)

    # Remove the temporary saved image.
    os.remove(temp_img)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
