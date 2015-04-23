from django.conf.urls import include, url
from django.contrib import admin
from bah_api import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rates/(?P<MHA>([A-Z]{2}[0-9]{3}))/$', views.rate_detail),
    url(r'^rates/(?P<Zip>([0-9]{5}))/$', views.zip_rates),
]
