from django.urls import path, include
from posts import views
from posts.views import MyRedirectView, counter_view

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('counter/', counter_view, name='counter'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('post/', include([
        path('add/', views.CreatePost.as_view(), name='add-post'),
        path('approve/<int:pk>/', views.approve_post, name='approve-post'),
        path('edit/<int:pk>/', views.EditPost.as_view(), name='edit-post'),
        path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete-post'),
        path('details/<int:pk>/', views.PostDetails.as_view(), name='post-details'),
    ])),
    path('redirect/', MyRedirectView.as_view())
]

