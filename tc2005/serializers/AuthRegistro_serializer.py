from rest_framework import serializers

from tc2005.models import AuthRegistro





class AuthRegistroSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthRegistro
        fields = "__all__"

class tokenSerializer(serializers.Serializer):

    token = serializers.CharField(

        required=True,
        
    )