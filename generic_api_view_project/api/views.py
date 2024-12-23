from django.shortcuts import render
from .models import Post, Comment, MediaPost
from .serializers import PostSerializer, UserCreateSerializer, UserLoginSerializer, CommentSerializer, MediaPostSerializer
from rest_framework import status # type: ignore
from rest_framework.response import Response # type: ignore
from django.contrib.auth import login 
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView  # type: ignore
from rest_framework.permissions import IsAuthenticatedOrReadOnly # type: ignore
from rest_framework.pagination import PageNumberPagination # type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore
from django.shortcuts import redirect
from django.db.models import Q 
from django.urls import reverse
from rest_framework.parsers import MultiPartParser, FormParser # type: ignore

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
            # 修正: reverse() で URL を取得してリダイレクト
            return redirect(reverse('api:post_api_view'))
        return Response('リクエストが間違っています', status=status.HTTP_400_BAD_REQUEST)
    
class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # 編集のログ保存や編集履歴の処理が必要な場合はここに追加
        serializer.save()
        
class CommentSearchAPIView(ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # クエリパラメータの取得
        query = self.request.query_params.get('q', '')  # 検索キーワード
        post_id = self.request.query_params.get('post_id', None)  # 投稿IDで絞り込み

        # ベースのクエリセット
        queryset = Comment.objects.all()

        # キーワード検索
        if query:
            queryset = queryset.filter(Q(comment__icontains=query))

        # 投稿IDによるフィルタリング
        if post_id:
            queryset = queryset.filter(post_id=post_id)

        return queryset
    
class MediaPostAPIView(ListCreateAPIView):
    queryset = MediaPost.objects.all()
    serializer_class = MediaPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]  # 追加: ファイルアップロード対応

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        # データの保存時に author を明示的に指定
        serializer.save(author=self.request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
