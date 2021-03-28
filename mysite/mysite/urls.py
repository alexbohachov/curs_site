from django.contrib import admin
from django.urls import path
from article.views import index, create, detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('article/create', create, name='create'),
    path('article/<int:article_id>', detail, name='detail'),
 ]