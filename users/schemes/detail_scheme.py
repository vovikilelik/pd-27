from django.db.models import Count, Case, When, Q

from ads.models import Ad
from lib.serialization.scheme import Scheme
from users.models import User


class DetailScheme(Scheme[User]):
    id: int
    first_name: str
    last_name: str
    username: str
    role: str
    age: int

    @classmethod
    def locations(cls, user):
        return [location.name for location in user.locations.all()]

    @classmethod
    def published(cls, user):
        ads = Ad.objects.filter(author_id=user.id, is_published=True)

        return len(ads)
