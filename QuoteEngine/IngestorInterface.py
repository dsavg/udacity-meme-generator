"""
Define IngestorInterface Class.

The DocxIngestor, PDFIngestor, CSVIngestor, and TextIngestor classes
realize the IngestorInterface abstract base class.
"""
import os
import random
import subprocess
from typing import List
from abc import ABC, abstractmethod

import docx
import pandas as pd

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """An abstract method for parsing file content."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Simple Ingestion check.

        :param path: A string path to a file containing quotes data.
        :return: True if it can be ingested.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Simply define parse method."""
        pass


class DocxImporter(IngestorInterface):
    """
    Ingest Doc file types using docx library.

    The class inherits the IngestorInterface.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Parse quotes from a Doc file using docx library.

        :param path: A string path to a file containing quotes data.
        :return: A list of valid QuoteModel.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text != '':
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0].replace('"', '').strip().strip('﻿'),
                                       parse[1].strip())
                quotes.append(new_quote)
        return quotes


class TXTImporter(IngestorInterface):
    """
    Ingest text file types.

    The class inherits the IngestorInterface.
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from a text.

        :param path: A string path to a file containing quotes data.
        :return: A list of valid QuoteModel.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, "r", encoding="utf-8") as file_ref:
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    new_quote = QuoteModel(parse[0].replace('"', '')
                                                   .strip()
                                                   .strip('﻿'),
                                           parse[1].strip())
                    quotes.append(new_quote)

        return quotes


class PDFImporter(IngestorInterface):
    """
    Ingest PDF file types using pdftotext.

    The class inherits the IngestorInterface.
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from a PDF file using pdftotext.

        :param path: A string path to a file containing quotes data.
        :return: A list of valid QuoteModel.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp/{random.randint(0,100000000)}.txt'
        subprocess.call(['pdftotext', '-layout', path, tmp])
        quotes = TXTImporter.parse(tmp)
        os.remove(tmp)
        return quotes


class CSVImporter(IngestorInterface):
    """Ingest CSV files using the pandas library.

    The class inherits the IngestorInterface.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from a CSV file using pandas.

        :param path: A string path to a file containing quotes data.
        :return: A list of valid QuoteModel.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        dataframe = pd.read_csv(path)

        for _, row in dataframe.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
        return quotes
