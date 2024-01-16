from django.urls import path
from .views import *

urlpatterns = [
    path('', MealGet.as_view()),
    path('<int:pk>', MealGet.as_view()),
    path('meals', MealGetList.as_view()),
    path('meals/<int:pk>', MealOne.as_view()),
    path('products', ProductGet.as_view()),
    path('products/<int:pk>', ProductGet.as_view()),
]