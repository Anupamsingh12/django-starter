from django.urls import path,re_path
# from django.conf.urls import re_path
from . import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    

     path('blog/', views.BlogPost.as_view(), name='blog-list-create'),
    path('hello/', views.HelloView.as_view(), name ='hello'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
