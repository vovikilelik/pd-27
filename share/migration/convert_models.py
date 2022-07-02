from categories.models import Category
from locations.models import Location
from share.migration.csv_to_model import csv_to_model
from share.utils.db_utils import create_ad_model, create_user_model

FILE_NAME_ADS = './datasets/ad.csv'
FILE_NAME_CATEGORIES = './datasets/category.csv'
FILE_NAME_LOCATIONS = './datasets/location.csv'
FILE_NAME_USERS = './datasets/user.csv'


def dict_to_ad(item):
    ad = create_ad_model(item)
    ad.save()


def dict_to_cat(item):
    category = Category()

    category.id = item['id']
    category.name = item['name']

    category.save()


def dict_to_location(item):
    location = Location()

    location.id = item['id']
    location.name = item['name']
    location.lat = item['lat']
    location.lon = item['lng']

    location.save()


def dict_to_user(item):
    user = create_user_model(item)
    user.save()


def convert_models():
    csv_to_model(FILE_NAME_CATEGORIES, dict_to_cat)
    csv_to_model(FILE_NAME_LOCATIONS, dict_to_location)
    csv_to_model(FILE_NAME_USERS, dict_to_user)
    csv_to_model(FILE_NAME_ADS, dict_to_ad)
