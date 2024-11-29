from django.urls import path
from .views import PostAPIView, UserCreateAPIView, UserLoginAPIView

app_name = 'api'

urlpatterns = [
    path('posts/', PostAPIView.as_view(), name='post_api_view'),
    path('signup/', UserCreateAPIView.as_view(), name='user_create_api_view'),
    path('login/', UserLoginAPIView.as_view(), name='user_login_api_view'),
]
