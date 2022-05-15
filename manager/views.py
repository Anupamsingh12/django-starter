from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from .models import News as blog
from .models import Categories as category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
  
  
class HelloView(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        content = {'message': 'Hello, world','user':request.user.username}
        return Response(content)

class NewsPost(APIView):
    # permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        fetch_size=10
        start_index=0
        end_index = start_index + fetch_size
        if 'fetch_size' in request.query_params:
            fetch_size = int(request.query_params['fetch_size'])
        if 'start_index' in request.query_params:
            start_index= int(request.query_params['start_index'])
        # print(startIndex)
        queryset=''
        if 'category_id' in request.query_params:
            category_id=int(request.query_params['category_id'])
            queryset = blog.objects.filter(category_id=category_id).order_by('-date_published').values('id','title','category_id')
        else:
            queryset = blog.objects.order_by('-date_published').select_related('category').values('id','title','category_id','category__name')

        size = queryset.count()
       
        paginator = PageNumberPagination()
        paginator.page_size = int(fetch_size)
        result_page = paginator.paginate_queryset(queryset, request)[start_index:end_index]
        len(result_page)
        content = {'fetch_size':int(fetch_size),"total_records":size,'records':len(result_page),'blogs': result_page}
        return Response(content)


class Categories(APIView):
    # permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        fetchSize=10
        startIndex=0
        endIndex = startIndex + fetchSize
        if 'fetchSize' in request.query_params:
            fetchSize = request.query_params['fetchSize']
        if 'startIndex' in request.query_params:
            startIndex= int(request.query_params['startIndex'])
        print(startIndex)
        queryset = category.objects.all().values()
        size = queryset.count()
       
        paginator = PageNumberPagination()
        paginator.page_size = int(fetchSize)
        result_page = paginator.paginate_queryset(queryset, request)[startIndex:endIndex]
        len(result_page)
        content = {'fetchSize':int(fetchSize),"totalRecords":size,'records':len(result_page),'categories': result_page}
        return Response(content)


class FOF(APIView):
    def get(self,request):
        return HttpResponse("<div style='text-align:center;'><h1>Nothing to serve here..</h1><br><h3>please send request at the provided endpoints</h3></div>")


class NewsPostById(APIView):
    # permission_classes = (IsAuthenticated, )
  
    def get(self, request,news_id):
        queryset = blog.objects.filter(id=news_id).select_related('NewsImage','Categories','User').values('id','title','body','date_published','date_updated','author_id','category_id','newsimage__id','newsimage__Img','author__first_name','author__last_name','author__email')
       
        paginator = PageNumberPagination()
        paginator.page_size = 1
        result_page = paginator.paginate_queryset(queryset, request)[0:1]
        content = {'news': result_page}
        return Response(content)
