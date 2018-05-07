from django.conf.urls import url
from AXF import views

urlpatterns = [
    url(r'^home/home/', views.home),
    url(r'^user/login/', views.login),
]