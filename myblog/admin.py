from django.contrib import admin
from myblog.models import Post
from myblog.models import Category

#admin.site.register(Post)
admin.site.register(Category)

class CategoriesInline(admin.TabularInline):
	model = Category.posts.through

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	inlines = [CategoriesInline]
# Register your models here.
