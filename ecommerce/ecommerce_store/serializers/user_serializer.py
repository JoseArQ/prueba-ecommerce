from rest_framework import serializers

from ecommerce_store.models import EcommerceUser

class EcommerceStoreListingField(serializers.RelatedField):
    """
    This class is for serializer relations from user to stores
    """

    def to_representation(self, value):
        """overwrite representation ecommerce"""
        pass
    
class EcommerceUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EcommerceUser
        fields = ('id', 'username', 'email')