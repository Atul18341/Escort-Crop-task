from rest_framework.response import Response
from rest_framework.views import APIView
from .serialization import AccountLedgerSerializers
from .models import AccountLedgerDetails
# Create your views here.

class AccountLedgerView(APIView):
    def get(self,request):
        queryset=AccountLedgerDetails.objects.all()
        serializers=AccountLedgerSerializers(queryset,many=True)
        return Response(serializers.data)