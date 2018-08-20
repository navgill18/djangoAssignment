from django.shortcuts import render
from myblog.models import Post
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import ListView

"""
def list_view(request):
	published = Post.objects.exclude(published_date__exact = None)
	posts = published.order_by('-published_date')
    context = {'posts': posts}
	return render(request, 'list.html', context)
"""

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
