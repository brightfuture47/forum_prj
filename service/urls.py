from django.urls import path
from service import views

urlpatterns = [
    path('', views.PostsView.as_view(), name='index'),
    path('post/<int:pk>', views.DetailPostsView.as_view(), name='detail_post'),
    path('about', views.about, name='about'),
]
