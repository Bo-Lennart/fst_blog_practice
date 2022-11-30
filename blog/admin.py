from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteInlineModelAdmin



@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('content')

# Register your models here.

