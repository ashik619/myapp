from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from rest_framework import generics
from .serializers import PostSerializer

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
	
class RESTpostapi(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer