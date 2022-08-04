"""Class to encapsulate the body and author of the quotes."""


class QuoteModel():
    """Class to encapsulate the body and author of the quotes.
    
    Each quote has two parts: body and author. These are provided during
    initialization. 

    :param body: body of the quote.
    :param author: author of the quote.
    """

    def __init__(self, body: str = '', author: str = ''):
        """To initialize a QuoteModel object.
        
        :param body: body of the quote.
        :param author: author of the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """To print in debugger friendly format."""
        return f"<<{self.body}, {self.author}>>"

    def __str__(self) -> str:
        """To print in human friendly format."""
        return f"'{self.body}, {self.author}"
