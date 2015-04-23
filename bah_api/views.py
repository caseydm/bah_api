from .models import withDependents, withOutDependents, ZipMHA
from .serializers import withDependentsSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# get BAH rates based on MHA
@api_view(['GET'])
def rate_detail(request, MHA):
    """
    Retrieve BAH rates
    """
    try:
        rates = withDependents.objects.get(MHA=MHA)
    except withDependents.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = withDependentsSerializer(rates)
        return Response(serializer.data)

@api_view(['GET'])
def zip_rates(request, Zip):
    """
    Retrieve BAH rates based on zip code
    """
    try:
        my_MHA = ZipMHA.objects.get(ZipCode = Zip)
        rate2 = withDependents.objects.get(MHA = my_MHA.MHA)
    except withDependents.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = withDependentsSerializer(rate2)
        return Response(serializer.data)