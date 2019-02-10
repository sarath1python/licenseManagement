from rest_framework import viewsets
from .models import Licensee
from .serializers import LicenseeSerializer


# ViewSets define the view behavior.
class LicenseeViewSet(viewsets.ModelViewSet):
    queryset = Licensee.objects.all()
    serializer_class = LicenseeSerializer
    page_size_query_param = 'page_size'
