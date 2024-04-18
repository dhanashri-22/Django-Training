from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from user_app.api.serializers import RegisterSerializer
from user_app import models
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def loguot_view(request):
    if request.method =='POST':
        request.user.auth.token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            # serializer.save()
            # data['username'] =account.username
            # data['email'] =account.email

            data['username'] = RegisterSerializer.validated_data['username']
            data['email'] = RegisterSerializer.validated_data['email']
               
            account = RegisterSerializer.save()

            # token = token.objects.get(user=account).key
            # data['token'] = token

            refresh = RefreshToken.for_user(account)

            data['token'] ={
                'refresh': str(refresh),
                'access' : str(refresh.access_token),
            }
        else:
            data=serializer.errors
        
        return Response(serializer.data)