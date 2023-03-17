from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommerce_store.models import EcommerceUser
from ecommerce_store.serializers.user_serializer import EcommerceUserSerializer

def is_valid_body(expected_body : list, body : dict)->bool:
    for param in expected_body:
        if not param in body.keys():
            return False
    
    return True

BODY_PARAMS = ['username', 'email']
class EcommerceUserAPIView(APIView):
    """
    ApiView for CRUD operations for EcommerceUser model 
    """
   
    def get(self, request, format=None):
        """
        Method for response user get http request.

        Returns:
            json response with next fields:
                - succes. bool. Flag that indicate if request end succesfully.
                - message. str. Information about reques procesed.
                - data. List[dict]. List with the all user found.
        """
        status_response = None
        try:
            users = EcommerceUser.objects.all()
            user_serializer = EcommerceUserSerializer(users, many=True)
            response = {
                'succes': True,
                'data': user_serializer.data
            }
            status_reponse = status.HTTP_200_OK
        except Exception as e:
            response = {
                'succes': False,
                'message': f'Error listing users: {e}'
            }
            status_reponse = status.HTTP_400_BAD_REQUEST
        
        
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
            # TODO: validate email field

            user = EcommerceUser.objects.create(**data)
            user_serializer = EcommerceUserSerializer(user)
            response = {
                "succes": True,
                "message": "user create successfully",
                "data": user_serializer.data
            }
            status_response = status.HTTP_201_CREATED
        except Exception as e:
            response = {
                "succes": False,
                "message": f"Error creating user: {e}",
                "data": None
            }
            status_response = status.HTTP_201_CREATED

        return Response(
            data=response,
            status=status_response
        )

class EcommerceUserDetailAPIView(APIView):

    def get(self, request, pk=None, format=None):
        """
        Method for response user get http request.

        Returns:
            json response with next fields:
                - succes. bool. Flag that indicate if request end successfully.
                - message. str. Information about reques processed.
                - data. dict. dict with information for an user specified.
        """
        status_reponse = None
        try:
            # user = get_object_or_404(self.users, pk)
            user = EcommerceUser.objects.get(pk=pk)
            print(f'get specific user: {user}')
            user_serializer = EcommerceUserSerializer(user)
            response = {
                'succes': True,
                'data': user_serializer.data
            }
            status_reponse = status.HTTP_200_OK
        except Exception as e:
            print(f"Error not found user: {e}")
            response = {
                'succes': False,
                'message': f"Error not found user: {e}"
            }
            status_reponse = status.HTTP_400_BAD_REQUEST

        return Response(
            data=response,
            status=status_reponse
        )

    def patch(self, request, pk=None):
        status_reponse = None
        try:
            data = request.data
            is_valid = is_valid_body(expected_body=BODY_PARAMS, body=data)
            user = EcommerceUser.objects.get(pk=pk)
            user.username = data.get('username')
            user.email = data.get('email')
            user.save()
            user_serializer = EcommerceUserSerializer(user)
            response = {
                'succes': True,
                'message': "user update successfully",
                'data': user_serializer.data
            }
            status_reponse = status.HTTP_200_OK
        except Exception as e:
            response = {
                'succes': False,
                'message': f"Error updating user: {e}",
                'data': None
            }
            status_reponse = status.HTTP_400_BAD_REQUEST
        
        return Response(
            data=response,
            status=status_reponse
        )