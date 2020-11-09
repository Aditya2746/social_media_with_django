from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('newpost/', views.new_post, name='new_post'),
    path('<uuid:post_id>', views.post_details, name='postdetails'),
    path('tags/<slug:tag_slug>', views.tags, name='tags'),
    path('<uuid:post_id>/like', views.like, name='postlike'),
    path('<uuid:post_id>/favorite', views.favorite, name='postfavorite'),
]
