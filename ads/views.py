import json

from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

from ads.models import Ad

from ads.schemes.ad_detail_scheme import AdDetailScheme
from ads.schemes.ad_short_scheme import AdShortScheme
from share.schemes.list_request import ListRequestScheme
from share.utils.db_utils import create_ad_model
from share.utils.request_utils import filter_or_not


class Hello(View):

    def get(self, request):
        # convert_models()

        return HttpResponse('ok', status=200)


@method_decorator(csrf_exempt, name='dispatch')
class Ads(View):

    def get(self, request):
        request_data = ListRequestScheme.serialize(request)

        ads = filter_or_not(Ad.objects.all(), request_data['query'], 'name', 'description')

        paginator = Paginator(ads.order_by(*request_data['order_by']), request_data['size'])
        page = paginator.page(request_data['page'])

        return JsonResponse(
            {
                'items': [AdShortScheme.serialize(i) for i in page],
                'page': page.number,
                'total': paginator.count
            },
            safe=False
        )


@method_decorator(csrf_exempt, name='dispatch')
class AdDetail(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse(AdDetailScheme.serialize(ad))


@method_decorator(csrf_exempt, name='dispatch')
class AdDelete(DeleteView):
    model = Ad

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()

        return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdCreate(CreateView):
    model = Ad

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        ad = create_ad_model(data)
        ad.save()

        return JsonResponse(AdDetailScheme.serialize(ad))


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdate(UpdateView):
    model = Ad

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)

        if 'id' not in data:
            return JsonResponse({'status': 'Bad request'}, status=400)

        ad = create_ad_model(data)
        ad.save()

        return JsonResponse(AdDetailScheme.serialize(ad))


@method_decorator(csrf_exempt, name='dispatch')
class AdImageUpload(UpdateView):
    model = Ad
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        ad = self.get_object()

        ad.image = request.FILES["image"]
        ad.save()

        return JsonResponse(AdDetailScheme.serialize(ad))
