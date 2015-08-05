from .models import withDependents, withOutDependents, ZipMHA
from .serializers import withDependentsSerializer, BAHSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def rates(request, zip_code, with_or_without):
    """
    Retrieve BAH rates based on zip code
    """
    if with_or_without == 'with':
        d = withDependents
    else:
        d = withOutDependents
    try:
        my_MHA = ZipMHA.objects.get(ZipCode=zip_code)
        rate2 = d.objects.get(MHA=my_MHA.MHA)
    except withDependents.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = withDependentsSerializer(rate2)
        return Response(serializer.data)


@api_view()
def test(request):
    MHA = ZipMHA.objects.get(ZipCode='31088')
    rate = withDependents.objects.get(MHA=MHA)
    serializer = BAHSerializer(rate)
    return Response(serializer.data)
