from ads.models import Ad
from lib.serialization.scheme import Scheme


class ShortScheme(Scheme[Ad]):
    id: int
    first_name: str
    last_name = str
    username: str
    role: str
