from django.urls import path
from django.conf.urls import url
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    SectionListView
)
from . import views

urlpatterns = [
    path('home', PostListView.as_view(), name='blog-home'),
    #section
    path('home/<str:section>', SectionListView.as_view(), name='section-home'),
    #section end
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about_detail, name='blog-about'),

    # url(r'^posts/(?P<postid>\d+)/preference/(?P<userpreference>\d+)/$', 
    #     views.postpreference, name='postpreference'),

    path('post/<int:pk>/preference/<int:userpreference>/', 
        views.postpreference, name='postpreference'),
]