from rest_framework import serializers

from ecommerce_store.models import EcommerceStore

class EcommerceUserListingField(serializers.RelatedField):
    """
    This class is for serializer relations between user and stores
    """

    def to_representation(self, value):
        """overwrite representation ecommerce user"""
        return {
            'user_id': value.id,
            'username': value.username,
            'email': value.email
        }

class EcommerceStoreSerializer(serializers.ModelSerializer):
    ecommerce_user = EcommerceUserListingField(read_only=True)

    class Meta:
        model = EcommerceStore
        fields = ('id', 'name', 'address', 'ecommerce_user')