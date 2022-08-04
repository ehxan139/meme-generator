"""Abstract class to all the ingestor classes."""

from abc import ABC
from abc import abstractmethod
from QuoteEngine.QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract class for all the ingestor classes."""

    allowed_extentions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """To check if the class can ingest the passed file.

        :param path: Path to the file
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extentions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        """Extract quotes from and returns a list of QuoteModel objects.

        :param path: Path to the file.
        """
        pass
