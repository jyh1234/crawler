
from django.contrib import admin
# from django.urls import path
from django.conf.urls import url,include


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^account/',include('account.urls', namespace='account')),
    url(r'^function/',include('function.urls',namespace='function')),
]