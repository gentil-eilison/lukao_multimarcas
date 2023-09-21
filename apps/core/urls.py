from django.urls import path
from apps.core import views


app_name = "core"
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login')
]