from .lib.csv_stream import CsvStream
from .lib.file_reader import FileReader


class Csv:
    file_name: str

    def __init__(self, file_name: str):
        self.file_name = file_name

    def as_dump(self):
        with open(self.file_name) as f:
            return f.readlines()

    def as_stream(self) -> CsvStream:
        return CsvStream(FileReader(open(self.file_name)))
