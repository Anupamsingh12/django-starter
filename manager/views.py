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

class BlogPost(APIView):
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
        queryset = blog.objects.all().order_by('-date_published').values()
        size = queryset.count()
       
        paginator = PageNumberPagination()
        paginator.page_size = int(fetchSize)
        result_page = paginator.paginate_queryset(queryset, request)[startIndex:endIndex]
        len(result_page)
        content = {'fetchSize':int(fetchSize),"totalRecords":size,'records':len(result_page),'blogs': result_page}
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