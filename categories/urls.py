from django.urls import path

from categories.views import Categories, CategoryDetail, CategoryDelete, CategoryCreate, CategoryUpdate

urlpatterns = [
    path('', Categories.as_view()),
    path('<int:pk>', CategoryDetail.as_view()),
    path('<int:pk>/delete/', CategoryDelete.as_view()),
    path('create/', CategoryCreate.as_view()),
    path('<int:pk>/update/', CategoryUpdate.as_view()),
]
