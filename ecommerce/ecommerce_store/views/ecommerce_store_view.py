from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ecommerce_store.models import EcommerceStore, EcommerceUser
from ecommerce_store.serializers.ecommerce_store_serializer import EcommerceStoreSerializer

BODY_PARAMS = ['user_id', 'name', 'address']

def is_valid_body(expected_body : list, body : dict)->bool:
    for param in expected_body:
        if not param in body.keys():
            return False
    
    return True

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
    
    def post(self, request, format=None):
        data = request.data
        try:
            is_valid = is_valid_body(expected_body=BODY_PARAMS, body=data)
            if not is_valid:
                raise Exception(f'required params {", ".join(BODY_PARAMS)}')
            print('valid request')
            user = EcommerceUser.objects.get(pk=int(data.get('user_id', None)))
            ecommerce = EcommerceStore.objects.create(
                ecommerce_user=user,
                name=data['name'],
                address=data['address']
            )
            ecommerce_serializer = EcommerceStoreSerializer(ecommerce)
            response = {
                "succes": True,
                "message": "ecommerce store create successfully",
                "data": ecommerce_serializer.data
            }
            status_response = status.HTTP_201_CREATED
        except Exception as e:
            response = {
                "succes": False,
                "message": f"Error creating ecommerce store: {e}",
                "data": None
            }
            status_response = status.HTTP_404_NOT_FOUND

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