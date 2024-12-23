from django.urls import path
from .views import PostAPIView, UserCreateAPIView, UserLoginAPIView, PostAPIDetailView, CommentListCreateAPIView, CommentRetrieveDestroyAPIView, CommentRetrieveUpdateDestroyAPIView, CommentSearchAPIView, MediaPostAPIView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'api'

urlpatterns = [
    path('posts/', PostAPIView.as_view(), name='post_api_view'),
    path('posts/<int:pk>/', PostAPIDetailView.as_view(), name='post_api_detail_view'),
    path('posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='comment_list_create_api_view'),
    path('posts/<int:post_id>/comments/<int:pk>/', CommentRetrieveDestroyAPIView.as_view(), name='comment_retrieve_destroy_api_view'),
    path('signup/', UserCreateAPIView.as_view(), name='user_create_api_view'),
    path('login/', UserLoginAPIView.as_view(), name='user_login_api_view'),
    path('posts/<int:post_id>/comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment_retrieve_update_destroy_api_view'),
    path('comments/search/', CommentSearchAPIView.as_view(), name='comment_search_api_view'),
    path('media-posts/', MediaPostAPIView.as_view(), name='media_post_api')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
