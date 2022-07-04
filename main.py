import json

from lib.csv.csv import Csv
from lib.serialization import fields

from lib.serialization.scheme import Scheme


class TestData:
    for_map_1 = 'for_map_1'
    for_map_2 = [1, 2, 3]

    one: str = '1000'
    two: str = 1000

    bundle = {'ant': 123}

    sets = ['1', '1', '2']

    lists = ['1', '2', '3']
    bundle_list = [{'ant': 123}, {'ant': 123}, {'ant': 123}]

    def getsome(self):
        return 'somev'


test_data = TestData()


class X(Scheme):
    ant: int

    @classmethod
    def is_x(cls, obj):
        return True


class A(Scheme[TestData]):
    one: int
    two: str

    lists: list

    bundle: X

    bundle_list: list

    @classmethod
    def obj_filed(cls, obj: TestData):
        return obj.bundle['ant'], '__random_filed_name'

    @classmethod
    def some(cls, obj: TestData):
        return obj.getsome()

    @classmethod
    def bundle_list_m(cls, obj: TestData):
        return [X.serialize(x) for x in obj.bundle_list]


def foo(o, *args):
    return 'def'


class B(A):
    field = 'zxc'

    field_lam = lambda o, n: 'field_lam'
    field_def = foo

    for_map_1 = fields.BasicField(custom_name='qqqqqq')
    for_map_1_any = fields.BasicField(key='for_map_1')

    for_map_2 = fields.IterableField(fields.BasicField())

    for_map_3 = fields.IterableField(X, key='bundle_list')

    def __init__(self, val):
        self._val = val

    @classmethod
    def some(cls, obj):
        return 'some override ' + A.some(obj)

    @classmethod
    def loo_class(cls, obj):
        return 'loo_class'


class BB(B):

    def loo_class(self, obj):
        return 'NOT loo_class'


ser = A.serialize(test_data)

ser_b = B('qwe').serialize(test_data)

print(ser)
print(json.dumps(ser))

print('')

print(ser_b)
print(json.dumps(ser_b))


class Proto:

    def proto(self):
        print('im from proto')


Foo = type(
    'MyClass',
    (Proto,),
    {
        'proto': lambda self: print('im from MyClass')
    }
)

p = Proto()
f = Foo()

p.proto()
f.proto()

print(-13 // 5)
print(-13 % 5)
