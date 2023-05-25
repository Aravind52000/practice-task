from django.shortcuts import render
from rest_framework import generics,permissions
from .models import User, Post, Like
from .serializers import UserSerializer, PostSerializer, LikeSerializer
#Get
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#post,update,delete
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#Get
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = [permissions.IsAuthenticated,IsPostPublicOrOwner]  
#post,update,delete
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = [permissions.IsAuthenticated,IsPostOwner]

#class IsPostOwner(permissions.BasePermission):
    #def has_object_permission(self, request, view, obj):
        #return obj.user == request.user

#class IsPostPublicOrOwner(permissions.BasePermission):
    #def has_object_permission(self, request, view, obj):
        #return obj.is_public or (request.user.is_authenticated and obj.user == request.user)
#Get
class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
#post,update,delete
class LikeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

