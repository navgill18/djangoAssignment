from django.urls import path

from .views import detail_view, BlogIndex #list_view

urlpatterns = [
	path('', BlogIndex.as_view(), name="blog_index"),
	path('posts/<int:post_id>/', detail_view, name = "blog_detail"),
]

#Added the following of AllAuth
#url(r'^accounts/', include('allauth.urls')),