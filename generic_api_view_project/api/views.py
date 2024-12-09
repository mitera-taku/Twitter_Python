from django.shortcuts import render
from .models import Post, Comment
from .serializers import PostSerializer, UserCreateSerializer, UserLoginSerializer, CommentSerializer
from rest_framework import status # type: ignore
from rest_framework.response import Response # type: ignore
from django.contrib.auth import login 
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView  # type: ignore
from rest_framework.permissions import IsAuthenticatedOrReadOnly # type: ignore

class CommentRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        user = self.request.user
        serializer.save(author=user, post_id = post_id)

class PostAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class PostAPIView(ListCreateAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    
    def get_queryset(self):
        posts = Post.objects.prefetch_related('comments').all()
        return posts
    
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
            