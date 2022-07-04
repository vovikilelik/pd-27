import json

from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView

from share.schemes.list_request import ListRequestScheme
from share.utils.db_utils import create_user_model
from share.utils.request_utils import filter_or_not
from users.models import User
from users.schemes.detail_scheme import DetailScheme


@method_decorator(csrf_exempt, name='dispatch')
class Users(View):

    def get(self, request):
        request_data = ListRequestScheme.serialize(request)

        ads = filter_or_not(User.objects.all(), request_data['query'], 'name')

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
class UserDetail(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse(DetailScheme.serialize(category))


@method_decorator(csrf_exempt, name='dispatch')
class UserDelete(DeleteView):
    model = User

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()

        return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class UserCreate(CreateView):
    model = User

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        user = create_user_model(data)
        user.save()

        return JsonResponse(DetailScheme.serialize(user))


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdate(UpdateView):
    model = User

    def put(self, request, *args, **kwargs):
        user = self.get_object()

        if not user:
            return JsonResponse({'status': 'Not Found'}, status=404)

        data = json.loads(request.body)

        user = create_user_model(data, user)
        user.save()

        return JsonResponse(DetailScheme.serialize(user))
