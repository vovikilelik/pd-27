from abs.models import Ad, Category
from utils.csv_to_model import csv_to_model

FILE_NAME_ADS = './datasets/ads.csv'
FILE_NAME_CAT = './datasets/categories.csv'


def dict_to_ad(dict):
    ad = Ad()

    ad.id = dict['id']
    ad.name = dict['name']
    ad.author = dict['author']
    ad.price = dict['price']
    ad.description = dict['description']
    ad.address = dict['address']
    ad.is_published = dict['is_published'] == 'TRUE'

    ad.save()


def dict_to_cat(dict):
    category = Category()

    category.id = dict['id']
    category.name = dict['name']

    category.save()


def convert_models():
    csv_to_model(FILE_NAME_ADS, dict_to_ad)
    csv_to_model(FILE_NAME_CAT, dict_to_cat)
