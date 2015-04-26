from django.conf.urls import include, url
from django.contrib import admin
from bah_api import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<zip_code>([0-9]{5}))/(?P<with_or_without>(\w+))/$', views.rates),
]