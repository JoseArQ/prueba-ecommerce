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
    
    # def validate_email(self, value):
    #     print("tipo: ",type(value))
    #     if not value:
    #         raise serializers.ValidationError("username value not found")
    
    # def validate(self, attrs):
    #     return attrs
    class Meta:
        model = EcommerceUser
        fields = ('id', 'username', 'email')