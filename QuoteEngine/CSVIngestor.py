"""Extracts quotes (body and author) from PDF files.

The `parse` function takes in a PDF file and extracts all the quotes in that. 

This class is encapsulated by the `Ingestor` class which then builts a database
of quotes returned by this.
"""

from pandas import read_csv

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Class to support extracting quotes from CSV files.
    
    Each extracted quote is saved as a QuoteModel object with a body and an 
    author. `parse` function extracts the quote and then returns list of the
    QuoteModel objects
    """

    allowed_extentions = ['csv']

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        """Extract quotes from PDF and returns a list of QuoteModel objects.

        :param path: Path to the PDF file.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes_list = []
        df = read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes_list.append(new_quote)

        return quotes_list
