# Motivational Meme Generator

In this capstone Udacity project, we'll use Python - and the skills we've developed in this course - to create a meme generator.

## Overview

The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote.

## Available Files
The project contains several files and folders.  
├── MemeEngine  
│   └── MemeEngine.py  
├── QuoteEngine  
│   ├── Ingestor.py  
│   ├── IngestorInterface.py  
│   └── QuoteModel.py  
├── README.md  
├── _data  
├── app.py  
├── fonts  
├── meme.py  
├── requirements.txt  
├── static  
├── templates  
├── tests  
│   ├── __init__.py  
│   ├── test_Ingestor.py  
│   ├── test_MemeEngine.py  
│   └── test_QuoteModel.py  
└── tmp   
Document details can be found bellow, 
* `meme.py` The main Python script that wraps the command-line tool, invokes the functions and classes available in this folder.
* `app.py` The main Python script to create the Flask app.  
* `MemeEngine.MemeEngine.py` contains the `MemeEngine` class with the ability to load, transform, and add captions to an image.
* `QuoteEngine.Ingestor.py` contains the `Ingestor`, which encapsulate ingestors to one interface for supported file types.
* `QuoteEngine.IngestorInterface.py` contains the `DocxIngestor`, `PDFIngestor`, `CSVIngestor`, and `TextIngestor` classes
which all realize the IngestorInterface abstract base class.
* `QuoteEngine.QuoteModel.py` contains the `QuoteModel` class, which has text fields for body and author a and prints the model contents as: ”body text” - author

Additionally, the project includes unit tests that will help test common cases under the `test` folder and can be run with `$ python3 -m unittest --verbose`

## Set-up
1. Set up a virtual environment
```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```
2. Install dependencies available in this repo
```bash
$ pip install -r requirements.txt
```
Additionally, the project uses the [Xpdf tool](https://www.xpdfreader.com/index.html) to process pdf files. Depending on your system, install the tool with the commands provided bellow

**Mac/Linux**  
```$ brew install xpdf```  
or  
```$ sudo apt-get install -y xpdf``` 

**Windows**  
[Find more here](https://www.xpdfreader.com/download.html)

## Execution
### Build Flask App
To start the server, run:
```bash
$ export FLASK_APP=app.py
$ flask run --host 0.0.0.0 --port 3000 --reload
```
### Use the Command-Line Interface tool
The project also included a cli tool to run the program on demand.

At a command line, you can run `python3 meme.py --help` for an explanation of how to invoke the script.
```bash
usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]

Generate a meme from an image file and some quote

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      path to an image file
  --body BODY      quote body to add to the image
  --author AUTHOR  quote author to add to the image
```
Example execution,
```bash
$ python3 meme.py --path=./_data/photos/dog/pumbaa_1.jpg --body="Let's go 49ers" --author=Pumbaa
Meme is available in: ./tmp/meme_pumbaa_1.jpg
```
There are 3 optional inputs the tool `path`, `body`, and `author`.

## Development Testing
The repo contains unit tests for all developed modules in MemeEngine and QuoteEngine. To run these tests from the project root, run:
```bash
$ python3 -m unittest --verbose
```
