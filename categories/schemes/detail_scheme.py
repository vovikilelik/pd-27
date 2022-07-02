from categories.models import Category
from lib.serialization.scheme import Scheme


class DetailScheme(Scheme[Category]):
    id: int
    name: str
