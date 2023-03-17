from rest_framework import serializers

from ecommerce_store.models import EcommerceUser
    
class EcommerceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceUser
        fields = ('id', 'username', 'email')