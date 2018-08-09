from django.shortcuts import render
from myblog.models import Post

def list_view(request):
	published = Post.objects.exclude(published_date__exact = None)
	posts = published.order_by('-published_date')

	return render(request, 'list.html', {'posts':posts})

def detail_view(request, post_id):
	post = Post.objects.get(pk=post_id)

	return render(request, 'detail.html', {'post':post})
# Create your views here.
