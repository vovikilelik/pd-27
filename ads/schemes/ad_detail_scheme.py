from ads.models import Ad
from lib.serialization.scheme import Scheme


class AdDetailScheme(Scheme[Ad]):
    id: int
    name: str
    price = float
    description: str
    is_published: bool

    @classmethod
    def image(cls, ad):
        return ad.image.url if ad.image else None

    @classmethod
    def category(cls, ad):
        return ad.category.id

    @classmethod
    def author(cls, ad):
        return ad.author.id
