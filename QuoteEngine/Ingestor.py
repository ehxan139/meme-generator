"""Main class to encapsulate all the ingestor sub-classes.

`parse` function takes the list of available ingestors and a path to the file. 
Then it finds a compatible ingestor that can read the file and return the 
contents.
"""

from QuoteEngine import QuoteModel
from QuoteEngine import IngestorInterface
from QuoteEngine import DocxIngestor
from QuoteEngine import PDFIngestor
from QuoteEngine import CSVIngestor
from QuoteEngine import TextIngestor


class Ingestor(IngestorInterface):
    """Main class to encapsulate all the ingestor sub-classes."""

    importers = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        """Extract quotes from file and returns a list of QuoteModel objects.

        :param path: Path to the file.
        """
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
