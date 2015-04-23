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