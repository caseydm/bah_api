from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'bahproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^bah_api/', include('bah_api.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('bah_api.urls')),
]
