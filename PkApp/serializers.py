from .models import Org, Seq, OrgSubdom, Auth
from rest_framework import serializers


class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org
        fields = '__all__'

class SeqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seq
        fields = '__all__'

class OrgSubdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgSubdom
        fields = '__all__'

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = '__all__'