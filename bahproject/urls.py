from django.conf.urls import include, url
from django.contrib import admin
from bah_api.models import BAH
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class BAHSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BAH
        fields = ('rank', 'dependents', 'MHA', 'rate')

# ViewSets define the view behavior.
class BAHViewSet(viewsets.ModelViewSet):
    queryset = BAH.objects.all()
    serializer_class = BAHSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'BAH', BAHViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
