from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('code_page/',  views.code_page,  name="code_page")
]