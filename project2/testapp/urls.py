from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView, PostListCreateView, PostRetrieveUpdateDestroyView, LikeListCreateView, LikeRetrieveUpdateDestroyView

urlpatterns = [
    path('users/', UserListCreateView.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view()),
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view()),
    path('likes/', LikeListCreateView.as_view()),
    path('likes/<int:pk>/', LikeRetrieveUpdateDestroyView.as_view()),
]
