from django.urls import path
from service import views

urlpatterns = [
    path('', views.PostsView.as_view(), name='index'),
    path('post/<int:pk>', views.DetailPostView.as_view(), name='detail_post'),
    path('create_post', views.CreatePostView.as_view(), name='create_post'),
    path('update_post/<int:pk>', views.UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<int:pk>', views.DeletePostView.as_view(), name='delete_post'),
    path('about', views.about, name='about'),
]
