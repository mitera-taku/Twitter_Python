from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer, UserCreateSerializer, UserLoginSerializer
from rest_framework import status # type: ignore
from rest_framework.response import Response # type: ignore
from django.contrib.auth import login 
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView # type: ignore
from rest_framework.permissions import IsAuthenticatedOrReadOnly # type: ignore

class PostAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # lookup_field = 'title'
    # lookup_url_kwarg = 'title'
    

class PostAPIView(ListCreateAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserCreateAPIView(CreateAPIView):
    
    model = User
    serializer_class = UserCreateSerializer
    
class UserLoginAPIView(GenericAPIView):
    
    serializer_class = UserLoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data, context={
            'request': request, 
        })
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            return Response('ログインしました', status=status.HTTP_202_ACCEPTED)
        return Response('requestが間違っています', status=status.HTTP_400_BAD_REQUEST)
            