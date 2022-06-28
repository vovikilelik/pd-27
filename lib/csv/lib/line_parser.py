from abc import ABC, abstractmethod


class LineParser(ABC):

    @abstractmethod
    def readline(self, text) -> list[str] | None:
        pass
