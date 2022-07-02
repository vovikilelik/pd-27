from typing import Callable, Any

from lib.csv.csv import Csv


def csv_to_model(file_name: str, reducer: Callable[[dict[str, str]], Any]):
    csv = Csv(file_name)

    with csv.as_stream() as stream:
        for row in stream.readobjects():
            reducer(row)
