import json

from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.views import View
from django.views.generic import DetailView

from abs.models import Category, Ad


class Hello(View):

    def get(self, request):
        return HttpResponse('ok', status=200)


class Categories(View):

    def get(self, request):
        categories = Category.objects.all()

        return JsonResponse(
            list(map(lambda e: {'id': e.id, 'name': e.name}, categories)),
            safe=False
        )

    def post(self, request):
        data = json.loads(request.body)

        category = Category()

        category.name = data['name']

        category.save()

        return JsonResponse({
            'id': category.id,
            'name': category.name
        })


class CategoryDetail(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            'id': category.id,
            'name': category.name
        })


class Ads(View):

    def get(self, request):
        ads = Ad.objects.all()

        return JsonResponse(
            list(map(lambda e: {'id': e.id, 'name': e.name, 'author': e.author, 'price': e.price}, ads)),
            safe=False
        )

    def post(self, request):
        data = json.loads(request.body)

        ad = Ad()

        ad.name = data['name']
        ad.author = data['author']
        ad.price = data['price']
        ad.description = data['description']
        ad.address = data['address']
        ad.is_published = data['is_published']

        ad.save()

        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author': ad.author,
            'price': ad.price,
            'description': ad.description,
            'address': ad.address,
            'is_published': ad.is_published,
        })


class AdDetail(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author': ad.author,
            'price': ad.price,
            'description': ad.description,
            'address': ad.address,
            'is_published': ad.is_published,
        })
