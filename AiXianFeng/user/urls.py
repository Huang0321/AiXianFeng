
from rest_framework.routers import SimpleRouter
from django.conf.urls import url
from user import views


router = SimpleRouter()
router.register(r'login_seri', views.LoginSerializers)

urlpatterns = [
    url(r"^regist/", views.regist, name='rg'),
    url(r"^login/", views.login, name='lgi'),
    url(r"^logout/", views.logout, name='lgo')
]

urlpatterns += router.urls