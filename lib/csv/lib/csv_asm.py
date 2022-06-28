from .reader import Reader
from .simple_line_parser import SimpleLineParser
from .line_parser import LineParser

DEFAULT_PARSER = SimpleLineParser()


class CsvAsm:
    _reader: Reader
    _columns: list[str]

    def __init__(self, reader: Reader, columns: list[str] = None):
        self._reader = reader
        self._columns = columns

    @property
    def reader(self):
        return self._reader

    @property
    def columns(self):
        return self._columns

    def readline(self, parser: LineParser = DEFAULT_PARSER) -> list[str] | None:
        if not self._columns:
            self._columns = parser.readline(self._reader)

        return parser.readline(self._reader)

    def readlines(self, parser: LineParser = DEFAULT_PARSER):
        while True:
            list_line = self.readline(parser)

            if not list_line:
                return

            yield list_line

    def readobjects(self, parser: LineParser = DEFAULT_PARSER):
        for list_line in self.readlines(parser):
            yield dict(zip(self._columns, list_line))
