from django.contrib import admin

from .models import Tag, Author, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields= {"slug": ("title")}
    list_filter = ("authors", "tag", "date")
    list_display= ("title","tag", "authors")

admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post)


