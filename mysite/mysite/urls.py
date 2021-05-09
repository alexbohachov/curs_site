from django.contrib import admin
from django.urls import path, include
from article.views import IndexView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView
from account.views import ProfileDetailView, SignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    # Article
    path('article/create', ArticleCreateView.as_view(), name='create'),
    path('article/<int:article_id>', ArticleDetailView.as_view(), name='detail'),
    path('article/update/<int:article_id>', ArticleUpdateView.as_view(), name='update'),
    path('article/delete/<int:article_id>', ArticleDeleteView.as_view(), name='delete'),
    # Account/Profile
    path('account/profile/<int:profile_id>', ProfileDetailView.as_view(), name='profile'),
    path('account/', include('django.contrib.auth.urls')),
    path('signup', SignUp.as_view(), name='signup')
 ]