from .models import Post
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .serializers import PostSerializer, PostCategorySerializer
from django.shortcuts import render, redirect
from .forms import Post, PostForm
from .models import User, PostCategory, Post
# Create your views here.
# create user
# posts = [
#     {'id': 1, 'name': 'Lets do it'},
#     {'id': 2, 'name': 'u r the best'},
#     {'id': 3, 'name': 'i WANT TO BE BEST'},

# ]


def home(request, title=None, content=None, category=None):

    if title:
        Posts = Post.objects.filter(title=title)
    
    elif content:
        Posts = Post.objects.filter(content=content)
    
    elif category:
        pc=PostCategory.objects.filter(category=category)
        
        Posts = Post.objects.filter(id__in=pc)
    
    else:
        Posts = Post.objects.all()
        
    
    context = {'posts': posts}
    return render(request, 'practiceform/home.html', context)


def posts(request, pk):
    posts = Post.objects.get(id=pk)

    return render(request, 'practiceform/post.html', context={'posts': posts})


def createpost(request):
    postform = PostForm()
    context = {'postform': postform}

    if request.method == 'POST':
        postform = PostForm(request.POST)
        if postform.is_valid():
            postform.save()
            return redirect('home')
    return render(request, 'practiceform/post_form.html', context)


def updatepost(request, pk):
    post = Post.objects.get(id=pk)
    print(post)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'postform': form}
    return render(request, 'practiceform/post_form.html', context)


def deletepost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'practiceform/delete.html', {'obj': post})


def categories(request):
    categories = PostCategory.objects.all()
    context = {'categories': categories}
    return render(request, 'practiceform/categories.html', context)


class PostList(APIView):

    def get(self, request, title=None, content=None, category=None, format=None):

        if title:
            Posts = Post.objects.filter(title=title)
            serializer = PostSerializer(Posts, many=True)
        elif content:
            Posts = Post.objects.filter(content=content)
            serializer = PostSerializer(Posts, many=True)
        elif category:
            pc=PostCategory.objects.filter(category_name=category)
            Posts = Post.objects.filter(id__in=pc)
            serializer = PostSerializer(Posts, many=True)
        else:
            Posts = Post.objects.all()
            serializer = PostSerializer(Posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Post = self.get_object(pk)
        serializer = PostSerializer(Post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Post = self.get_object(pk)
        serializer = PostSerializer(Post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Post = self.get_object(pk)
        Post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):

    def get(self, request, format=None):
        Posts = PostCategory.objects.all()
        serializer = PostCategorySerializer(Posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
