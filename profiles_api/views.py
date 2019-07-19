from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from profiles_api import serializers, models, permissions


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiView = ['A', 'B', 'C']
        return Response({'message': 'Hello', 'an_apiView': an_apiView})

    def post(self, request):
        searializer = self.serializer_class(data=request.data)
        if searializer.is_valid():
            name = searializer.validated_data.get('name')
            message = f'Hello {name} !!!'
            return Response({'message': message})
        else:
            return Response(
                searializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class HelloApiView2(APIView):
    serializer_class = serializers.HelloSerializer2

    def get(self, request, format=None):
        return Response({'message': 'Hello its API VIew 2'})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            return Response({
                'email': f'Email is {email}',
                'dob': serializer.validated_data.get('dob'),
                'isActive': serializer.validated_data.get('is_Active'),
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer2

    def list(self, request):
        a_viewset = ['A', 'B', 'C', 'D']
        return Response({'message': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            return Response({
                'email': f'Email is {email}',
                'dob': serializer.validated_data.get('dob'),
                'isActive': serializer.validated_data.get('is_Active'),
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated,
    )

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.PostItemSeializer
    queryset = models.Post.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)