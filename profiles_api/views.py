from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from profiles_api import models
from profiles_api import serializers
import uuid
import datetime
from django.core.mail import send_mail


class Login(ObtainAuthToken):
    """Handle auth token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class Logout(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class EmailConfirmation(APIView):
    def post(self, request, format=None):
        user_id = request.data['user_id']
        user = models.UserProfile.objects.filter(id=user_id)
        if user.count() > 0:
            user = user[0]
            t = uuid.uuid3(uuid.NAMESPACE_DNS, 'user'+str(user.id) +
                           user.email+str(datetime.datetime.now().timestamp()))
            send_mail('Confirm Email', 'Your account for Kamyab Learning System Has been successfully created. Please open this link to confirm your email  http://127.0.0.1:8000/api/email/?token=' +
                      str(t), 'hammad22ali@gmail.com', ['hammad11ali@gmail.com'])
            models.EmailToken.objects.create(
                user=user, token=t, usetype='emailconfirm')
            return Response({'message': 'ok'})
        else:
            return Response({'message': 'ok'})

    def get(self, request, format=None):
        if 'token' in request.query_params.keys():
            token = request.query_params['token']
            emailcheck = models.EmailToken.objects.filter(token=token)
            if emailcheck.count() > 0:
                emailcheck = emailcheck[0]
                if(emailcheck.usetype == 'emailconfirm'):
                    models.UserProfile.objects.filter(
                        id=emailcheck.user.id).update(is_enabled=True)
                emailcheck.delete()
                return Response({'message': 'ok'})
            else:
                return Response({'message': 'Invalid Token'})
        else:
            return Response({'message': 'No token'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)
