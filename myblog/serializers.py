from django.contrib.auth.models import User, Group
from rest_framework import serializers
from myblog.models import Post, Category

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('title', 'text', 'author', 'published_date', 'created_date','modified_date')

class CategorySerializer(serializers.ModelSerializer):
	model = Category
	fields = ('name', 'description', 'posts')