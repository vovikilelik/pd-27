import json

from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView

from ads.models import Category
from categories.schemes.detail_scheme import DetailScheme
from share.schemes.list_request import ListRequestScheme
from share.utils.request_utils import filter_or_not


@method_decorator(csrf_exempt, name='dispatch')
class Categories(View):

    def get(self, request):
        request_data = ListRequestScheme.serialize(request)

        ads = filter_or_not(Category.objects.all(), request_data['query'], 'name')

        paginator = Paginator(ads.order_by(*request_data['order_by']), request_data['size'])
        page = paginator.page(request_data['page'])

        return JsonResponse(
            {
                'items': [DetailScheme.serialize(i) for i in page],
                'page': page.number,
                'total': paginator.count
            },
            safe=False
        )


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreate(CreateView):
    model = Category

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        category = Category()
        category.name = data['name']
        category.save()

        return JsonResponse(DetailScheme.serialize(category))


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetail(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse(DetailScheme.serialize(category))


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDelete(DeleteView):
    model = Category

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()

        return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdate(UpdateView):
    model = Category

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)

        if 'id' not in data:
            return JsonResponse({'status': 'Bad request'}, status=400)

        category = Category()
        category.name = data['name']
        category.save()

        return JsonResponse(DetailScheme.serialize(category))

