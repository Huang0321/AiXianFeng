from django.conf.urls import url

from mine import views

urlpatterns = [
    url(r'mine_home/', views.mine_home, name='mh'),
    url(r'mine_not_pay/', views.not_pay, name='mnp'),
    url(r'mine_not_recieve', views.not_recieve, name='mnr'),
]