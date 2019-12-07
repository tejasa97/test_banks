from django.http import JsonResponse
from rest_framework import generics
from .models import Banks, Branches
from .serializers import BankSerializer, BranchSerializer

# Create your views here.
def handler404(request, exception=None):
    response = {
        'Error'   : "404",
        'Message' : "Page doesn't exist"
    }
    response.status_code = 404
    return JsonResponse(response)

class BranchIFSC(generics.RetrieveAPIView):

    serializer_class = BranchSerializer

    def get_object(self):

        ifsc_code = self.kwargs['ifsc']
        return Branches.objects.get(pk=ifsc_code)

class BranchFilter(generics.ListAPIView):

    serializer_class = BranchSerializer
    
    def get_queryset(self):

        bank = self.kwargs.get('bank').upper()
        city = self.kwargs.get('city').upper()

        limit  = int(self.request.query_params.get('limit', -1))
        offset = int(self.request.query_params.get('offset', 0))

        return Branches.objects.select_related('bank').filter(bank__name=bank, city=city)[offset:] if limit == -1 else Branches.objects.select_related('bank').filter(bank__name=bank, city=city)[offset:offset+limit]
