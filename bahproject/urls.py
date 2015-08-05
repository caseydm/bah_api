from django.conf.urls import url
from django.views.generic import TemplateView
from bah_api import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="bah_api/index.html")),
    url(r'^(?P<zip_code>([0-9]{5}))/(?P<with_or_without>(\w+))/$',
        views.rates),
]
