from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.default_map, name='default'),
]
