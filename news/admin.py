from django.contrib import admin
from .models import Article, Journalist

admin.site.register(Article)
admin.site.register(Journalist)
# admin.site.register(Comments)

# this is good information to go over thouroghly
# https://docs.djangoproject.com/en/1.10/ref/contrib/admin