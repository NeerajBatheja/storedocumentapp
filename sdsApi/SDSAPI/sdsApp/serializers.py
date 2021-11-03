from rest_framework import serializers
from sdsApp.models import SDS


class SDSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SDS
        fields=('folder','topic','document')
