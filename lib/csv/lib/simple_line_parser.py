from .line_parser import LineParser
from .reader import Reader

SEPARATORS = [';', ',']
QUOTES = ['"', '\'']
ESCAPE_CHAR = '\\'


def read_chars(text: str):
    last_quote = None
    start = 0

    for i in range(len(text)):
        char = text[i]

        if last_quote is None:
            if char in QUOTES:
                last_quote = char
                start = i + 1
            else:
                yield i, i + 1

        elif char == last_quote:
            last_quote = None
            yield start, i


def read_segment(reader: Reader):
    last_quote = None

    char_array = list()
    end_of_line = False

    while True:
        char = reader.read()

        if not char:
            end_of_line = True
            break

        if last_quote is None:
            if char in QUOTES:
                last_quote = char
                continue
            else:
                if char in SEPARATORS:
                    break
                elif char == '\n':
                    end_of_line = True
                    break

        elif char == last_quote:
            last_quote = None
            continue

        char_array.append(char)

    return ''.join(char_array), end_of_line


def read_row(reader: Reader):
    while True:
        segment, end_of_line = read_segment(reader)

        if not segment and end_of_line:
            return

        yield segment

        if end_of_line:
            return


class SimpleLineParser(LineParser):

    def readline(self, reader: Reader) -> list[str] | None:
        columns = list(read_row(reader))
        return columns if len(columns) else None
