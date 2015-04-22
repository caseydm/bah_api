from .models import withDependents, withOutDependents, ZipMHA

from bah_api.serializers import withDependentsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# get BAH rates based on MHA
@csrf_exempt
def rate_detail(request, MHA):
    """
    Retrieve BAH rates
    """
    try:
        rates = withDependents.objects.get(MHA=MHA)
    except withDependents.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = withDependentsSerializer(rates)
        return JSONResponse(serializer.data)