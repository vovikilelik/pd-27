from ads.models import User, Ad, Category
from locations.models import Location


def create_user_model(data_dict, user=User()) -> User:
    if 'id' in data_dict:
        user.id = data_dict['id']

    user.first_name = data_dict['first_name']
    user.last_name = data_dict['last_name']
    user.username = data_dict['username']
    user.password = data_dict['password']
    user.role = data_dict['role']
    user.age = data_dict['age']

    if 'locations' in data_dict:
        user.save()
        user.locations.set(data_dict['locations'])

    return user


def create_ad_model(data_dict, ad=Ad()) -> Ad:
    if 'id' in data_dict:
        ad.id = data_dict['id']

    ad.name = data_dict['name']
    ad.price = data_dict['price']
    ad.description = data_dict['description']
    ad.is_published = data_dict['is_published'] == 'TRUE'

    ad.image = data_dict['image']

    ad.author = User.objects.get(pk=data_dict['author_id'])
    ad.category = Category.objects.get(pk=data_dict['category_id'])

    return ad
