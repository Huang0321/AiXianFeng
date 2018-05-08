from django.conf.urls import url
from AXF import views

urlpatterns = [
    url(r'^home/', views.home, name='home')
  ]