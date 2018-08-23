from django.shortcuts import render
from myblog.models import Post
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import ListView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from myblog.serializers import UserSerializer, GroupSerializer

"""
def list_view(request):
	published = Post.objects.exclude(published_date__exact = None)
	posts = published.order_by('-published_date')
    context = {'posts': posts}
	return render(request, 'list.html', context)
"""

class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class BlogIndex(ListView):
	template_name = 'list.html'
	context_object_name = 'posts'
	queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
	#model = Post

def detail_view(request, post_id):
	published = Post.objects.exclude(published_date__exact = None)
	try:
		post = Post.objects.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404
	context = {'post':post}
	return render(request, 'detail.html', {'post':post})
# Create your views here.
