from django.conf.urls.static import static
from django.urls import path

from ads.views import Ads, AdDetail, AdImageUpload
from siesta import settings

urlpatterns = [
    path('', Ads.as_view()),
    path('<int:pk>', AdDetail.as_view()),
    path('<int:pk>/upload/', AdImageUpload.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
