from ads.models import Ad
from lib.serialization.scheme import Scheme
from users.models import User


class DetailScheme(Scheme[User]):
    id: int
    first_name: str
    last_name = str
    username: str
    role: str
    age: int

    @classmethod
    def location(cls, user):
        return user.location.id
