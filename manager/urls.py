from django.urls import path,re_path
# from django.conf.urls import re_path
from . import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    

     path('', views.FOF.as_view(), name='blog-list-create'),

     path('news/', views.NewsPost.as_view(), name='get-news-titles'),
     path('news/<int:news_id>', views.NewsPostById.as_view(), name='get-newsPost_by_id'),
     path('categories/', views.Categories.as_view(), name='news-category'),
    path('hello/', views.HelloView.as_view(), name ='hello'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
