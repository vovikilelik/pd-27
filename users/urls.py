from django.urls import path

from users.views import Users, UserDetail, UserDelete, UserCreate, UserUpdate

urlpatterns = [
    path('', Users.as_view()),
    path('<int:pk>', UserDetail.as_view()),
    path('<int:pk>/delete/', UserDelete.as_view()),
    path('create/', UserCreate.as_view()),
    path('<int:pk>/update/', UserUpdate.as_view()),
]
