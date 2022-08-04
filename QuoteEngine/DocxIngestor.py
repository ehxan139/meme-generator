"""Extracts quotes (body and author) from PDF files.

The `parse` function takes in a PDF file and extracts all the quotes in that. 

This class is encapsulated by the `Ingestor` class which then builts a database
of quotes returned by this.
"""

import docx

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Class to support extracting quotes from docx files.
    
    Each extracted quote is saved as a QuoteModel object with a body and an 
    author. `parse` function extracts the quote and then returns list of the
    QuoteModel objects
    """

    allowed_extentions = ['docx']

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        """Extract quotes from PDF and returns a list of QuoteModel objects.

        :param path: Path to the PDF file.
        """
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest, filetype not allowed.")

        quotes_list = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != '':
                parsed = para.text.split(" - ")
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes_list.append(new_quote)
        return quotes_list
