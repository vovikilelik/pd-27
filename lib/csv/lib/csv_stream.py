from typing import IO

from .csv_asm import CsvAsm
from .reader import Reader


class CsvStream:
    _reader: Reader
    _asm: CsvAsm

    def __init__(self, reader: Reader):
        self._reader = reader

    def __enter__(self) -> CsvAsm:
        return CsvAsm(self._reader)

    def __exit__(self, *args):
        self._reader.close()

    @property
    def assembler(self):
        return self._asm
