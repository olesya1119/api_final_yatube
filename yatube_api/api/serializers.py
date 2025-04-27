from rest_framework import serializers
from posts.models import Post, Comment, Group, Follow, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'text', 'created')
        read_only_fields = ('post', 'author', 'created')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate(self, data):
        user = data.get('user', self.context['request'].user)
        following = data['following']
        if user == following:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!')
        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя!')
        return data
