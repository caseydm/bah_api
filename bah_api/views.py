from .models import withDependents, withOutDependents, ZipMHA
from .serializers import BAHSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def rates(request, zip_code, with_or_without):
    """
    Retrieve BAH rates based on zip code
    """
    if with_or_without == 'with':
        d = withDependents
    else:
        d = withOutDependents
    try:
        MHA_query = ZipMHA.objects.get(ZipCode=zip_code)
        rate = d.objects.get(MHA=MHA_query.MHA)
    except d.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BAHSerializer(rate)
    return Response(serializer.data)
