from rest_framework import generics, permissions, status
from .models import Post
from .serializers import PostSerializer
from authentication.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import os
import json
from django.conf import settings


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# @api_view(['GET'])
# def getclubposts(request, *args, **kwargs):
#     club_username = request.data['username']
#     posts = Post.objects.get(username=club_username)
#     serializer = PostSerializer(data=posts)
#     return Response(serializer.data, status=status.HTTP_200_OK)


class UserPostsView(APIView):
    def get(self, request, username):
        posts = Post.objects.filter(user__username=username)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    

# PostCreate working => only clubs can create, users cannot. Media is stored as url 
class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        current_user = self.request.user # Get the current user
        if current_user.user_type == 'club' or current_user.user_type == 'Club':
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
        
        return Response("Forbidden: Only users with user_type='club' can create posts.", status=status.HTTP_403_FORBIDDEN)

# Get the path to your project's base directory
base_dir = settings.BASE_DIR

# Construct the path to the cache.json file
cache_file_path = os.path.join(base_dir, 'feed', 'cache', 'cache.json')
reg_file_path = os.path.join(base_dir, 'feed', 'cache', 'reg.json')
clubpost_file_path = os.path.join(base_dir, 'feed', 'cache', 'post.json')

with open(cache_file_path, 'r') as file:
    cacheData = json.load(file)

with open(reg_file_path, 'r') as file:
    regData = json.load(file)

with open(clubpost_file_path, 'r') as file:
    clubData = json.load(file)
    

class CheckPost(APIView):
    def get(self, request):
        return Response(cacheData) 


class RegPost(APIView):
    def get(self, request):
        return Response(regData)


class ClubPost(APIView):
    def get(self, request):
        return Response(clubData)