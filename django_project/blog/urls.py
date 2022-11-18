from django.urls import path
from psutil import users
from . import views
from users import views as userview
from django.conf import settings
from django.conf.urls.static import static
from .views import (PostListView,
    UserPostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView)
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',PostListView.as_view(),name="blog-home"),
    path('post/<int:pk>',PostDetailView.as_view(),name="post-detail"),
    path('post/new/',PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name="post-update"),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name="post-delete"),
    path('user/<str:username>/',UserPostListView.as_view(),name="user-posts"),
    path('about/',views.about,name="blog-about"),
    path('register/',userview.register,name="register"),
    path('profile/',userview.profile,name="profile"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name="logout"),
    
    path('base/',views.base,name="blog-base")
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)