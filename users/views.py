import json

from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from share.schemes.list_request import ListRequestScheme
from share.utils.db_utils import create_user_model
from share.utils.request_utils import filter_or_not
from users.models import User
from users.schemes.detail_scheme import DetailScheme
from users.schemes.short_scheme import ShortScheme


@method_decorator(csrf_exempt, name='dispatch')
class Users(View):

    def get(self, request):
        request_data = ListRequestScheme.serialize(request)

        ads = filter_or_not(User.objects.all(), request_data['query'], 'name')

        paginator = Paginator(ads.order_by(*request_data['order_by']), request_data['size'])
        page = paginator.page(request_data['page'])

        return JsonResponse(
            {
                'items': [ShortScheme.serialize(i) for i in page],
                'page': page.number,
                'total': paginator.count
            },
            safe=False
        )

    def post(self, request):
        data = json.loads(request.body)

        user = create_user_model(data)

        user.save()
        return JsonResponse(DetailScheme.serialize(user))


@method_decorator(csrf_exempt, name='dispatch')
class UserDetail(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse(DetailScheme.serialize(category))

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()

        return JsonResponse({'status': 'ok'}, status=200)

