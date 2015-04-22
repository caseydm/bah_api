from django.conf.urls import include, url
from django.contrib import admin
from bah_api import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rates/(?P<MHA>[A-Za-z]+)/$', views.rate_detail.as_view()),
]
