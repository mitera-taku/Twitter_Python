from rest_framework import serializers # type: ignore
from .models import Post
from django.contrib.auth import get_user_model, authenticate # type: ignore
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'created_at')
        read_only_fields = ('author', )
        

class UserCreateSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(style={'input_type': 'password'},
                                     write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = get_user_model()
        return user.objects.create_user(
            validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']   
        )
        
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError('ユーザー名とパスワードを両方入力してください')

        # リクエストオブジェクトをコンテキストから取得
        request = self.context.get('request')

        # ユーザー認証
        user = authenticate(request=request, username=username, password=password)

        if user is None:
            raise serializers.ValidationError('ログインできませんでした')
        
        # 認証が成功した場合、ユーザー情報を返す
        data['user'] = user
        return data