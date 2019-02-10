from rest_framework import viewsets

from .models import License, Violation
from .serializers import LicenseSerializer, ViolationSerializer


# ViewSets define the view behavior.
class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.filter(is_deleted=False)
    serializer_class = LicenseSerializer
    page_size_query_param = 'page_size'


# ViewSets define the view behavior.
class ViolationViewSet(viewsets.ModelViewSet):
    queryset = Violation.objects.filter(is_deleted=False)
    serializer_class = ViolationSerializer
    page_size_query_param = 'page_size'
