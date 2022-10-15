"""Package all ingestors into a main Ingestor class.

This class encapsulates all the ingestors to provide
one interface to load any supported file type.
"""
from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface, DocxImporter, \
    CSVImporter, PDFImporter, TXTImporter


class Ingestor(IngestorInterface):
    """
    Encapsulate ingestors to one interface for supported file types.
    """

    ingestors = [DocxImporter, CSVImporter, PDFImporter, TXTImporter]

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Use ingestor based on the appropriate file extension.

        :param path: A string path to a file containing quotes data.
        :return: A list of valid QuoteModel.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        ext = path.split('.')[-1]
        raise TypeError(f'invalid file type: expecting '
                        f'*.docx, *.csv, *.pdf, *.txt, *.{ext} was found')
