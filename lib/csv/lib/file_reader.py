from typing import IO

from .reader import Reader


class FileReader(Reader):
    _source: IO
    _buffered_line: str = ''
    _seek: int = 0

    def __init__(self, source: IO):
        self._source = source

    @property
    def source(self):
        return self._source

    def read(self) -> str | None:
        if self._seek >= len(self._buffered_line):
            self._buffered_line = self._source.readline()
            self._seek = 0

        if not self._buffered_line:
            return

        char = self._buffered_line[self._seek]
        self._seek += 1

        return char

    def close(self):
        return self._source.close()
