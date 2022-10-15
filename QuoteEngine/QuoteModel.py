"""The Quote Engine module ingests files that contain quotes.

For our purposes, a quote contains a body and an author:
"This is a quote body" - Author
"""


class QuoteModel:
    """
    Class that defines a QuoteMode object.

    Contains text fields for body and author.
    Prints the model contents as: ”body text” - author
    """

    def __init__(self,
                 body: str,
                 author: str
                 ):
        """
        Create a new `QuoteModel`.

        :param body: The body of the quote
        :param author: The author of the quote
        """
        if not isinstance(body, str):
            raise TypeError(f'"body" should be of type str, '
                            f'{type(body)} found')
        if not isinstance(author, str):
            raise TypeError(f'"author" should be of type str, '
                            f'{type(author)} found')

        self._body = body
        self._author = author

    def __repr__(self) -> str:
        """Return `str(self)`."""
        return f'"{self._body}" - {self._author}'

    @property
    def body(self):
        """Return body."""
        return self._body

    @property
    def author(self):
        """Return author."""
        return self._author
