from django.contrib import admin
from django.urls import path
from posts.views import index, new_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('new/', new_post, name="new_post"),
]
