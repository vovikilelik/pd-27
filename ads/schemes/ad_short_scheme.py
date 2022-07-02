from ads.models import Ad
from lib.serialization.scheme import Scheme


class AdShortScheme(Scheme[Ad]):
    id: int
    name: str
    price = float
    is_published: bool

    @classmethod
    def category(cls, ad):
        return ad.category.id

    @classmethod
    def author(cls, ad):
        return ad.author.id
