from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ecommerce_store.models import EcommerceStore
from ecommerce_store.serializers.ecommerce_store_serializer import EcommerceStoreSerializer

class EcommerceStoreApiView(APIView):
    
    def get(self, request, format=None):
        status_response = None
        try:
            ecommerces = EcommerceStore.objects.all()
            ecommerce_serializer = EcommerceStoreSerializer(ecommerces, many=True)
            status_response = status.HTTP_200_OK
            response = {
                'succes': True,
                'message': f"{len(ecommerces)} ecommerce store found",
                'data': ecommerce_serializer.data
            }
        except Exception as e:
            print(f"Error listing ecommerce store: {e}")
            status_response = status.HTTP_400_BAD_REQUEST
            response = {
                'succes': True,
                'message': f"Error listing ecommerce store: {e}",
                'data': ecommerce_serializer.data
            }
    
        return Response(
            data=response,
            status=status_response
        )

class EcommerceStoreDetailApiView(APIView):
    
    def get(self, request, pk=None, format=None):
        status_response = None
        try:
            ecommerces = EcommerceStore.objects.get(pk=pk)
            ecommerce_serializer = EcommerceStoreSerializer(ecommerces)
            status_response = status.HTTP_200_OK
            response = {
                'succes': True,
                'message': f"ecommerce store found",
                'data': ecommerce_serializer.data
            }
        except Exception as e:
            print(f"Error listing ecommerce store: {e}")
            status_response = status.HTTP_400_BAD_REQUEST
            response = {
                'succes': True,
                'message': f"Error listing ecommerce store: {e}",
                'data': None
            }
    
        return Response(
            data=response,
            status=status_response
        )