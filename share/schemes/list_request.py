from lib.serialization.scheme import Scheme
from share.utils.object_utils import get_or_default


class ListRequestScheme(Scheme):

    @classmethod
    def query(cls, data):
        return get_or_default(data, 'query')

    @classmethod
    def page(cls, data):
        return max(1, int(get_or_default(data, 'page', 1)))

    @classmethod
    def size(cls, data):
        return get_or_default(data, 'size', 10)

    @classmethod
    def order_by(cls, data):
        return get_or_default(data, 'order_by', [])
