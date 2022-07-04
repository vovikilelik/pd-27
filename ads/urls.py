from django.conf.urls.static import static
from django.urls import path

from ads.views import Ads, AdDetail, AdImageUpload, AdDelete, AdUpdate
from siesta import settings

urlpatterns = [
    path('', Ads.as_view()),
    path('<int:pk>', AdDetail.as_view()),
    path('<int:pk>/delete/', AdDelete.as_view()),
    path('create/', AdDelete.as_view()),
    path('<int:pk>/update/', AdUpdate.as_view()),
    path('<int:pk>/upload/', AdImageUpload.as_view()),
]
