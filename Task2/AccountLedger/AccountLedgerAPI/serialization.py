from rest_framework import serializers
from .models import AccountLedgerDetails

class AccountLedgerSerializers(serializers.ModelSerializer):
    class Meta:
        model=AccountLedgerDetails
        fields='__all__'