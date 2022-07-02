from django.urls import path

from users.views import Users, UserDetail

urlpatterns = [
    path('', Users.as_view()),
    path('<int:pk>', UserDetail.as_view()),
]
