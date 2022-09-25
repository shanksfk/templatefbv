from django.urls import path
from . import views

urlpatterns = [

    #CBV
    path('pl/', views.PostList.as_view(), name='pl'),
    path('pl/title=<str:title>', views.PostList.as_view(), name='pl'),
    path('pl/content=<str:content>', views.PostList.as_view(), name='pl'),
    path('pl/category=<str:category>', views.PostList.as_view(), name='pl'),
    path('pd/<int:pk>', views.PostDetail.as_view(), name='pd'),
    path('categories/', views.CategoryList.as_view(), name='pc'),

    #FBV
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    # path('home/title=<str:title>', views.home, name='home'),
    # path('home/content=<str:content>', views.PostList.as_view(), name='home'),
    # path('home/cateogry=<str:category>', views.PostList.as_view(), name='home'),

    path('post/<str:pk>', views.posts, name='post'),
    path('create-post/', views.createpost, name='create-post'),
    path('update-post/<str:pk>/', views.updatepost, name='update-post'),
    path('delete-post/<str:pk>/', views.deletepost, name='delete-post'),
    path('category/', views.categories, name='categories'),


]
