from django.shortcuts import render
from .models import Post, Comment
from .serializers import PostSerializer, UserCreateSerializer, UserLoginSerializer, CommentSerializer
from rest_framework import status # type: ignore
from rest_framework.response import Response # type: ignore
from django.contrib.auth import login 
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView  # type: ignore
from rest_framework.permissions import IsAuthenticatedOrReadOnly # type: ignore
from rest_framework.pagination import PageNumberPagination # type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore
from django.shortcuts import redirect

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
        
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3  # 1ページあたりのアイテム数
    page_size_query_param = 'page_size'  # クエリパラメータでページサイズを変更可能にする（任意）
    max_page_size = 10  # 最大ページサイズ（任意）

class PostAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10
    last_page_strings = ('l',)
    

class PostAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # 修正
    pagination_class = PostListPagination

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
            return redirect('post_api_view')  # 修正: リダイレクト
        return Response('リクエストが間違っています', status=status.HTTP_400_BAD_REQUEST)
    