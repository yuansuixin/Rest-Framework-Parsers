from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.views import APIView
from rest_framework.request import Request


# class ParamVersion(object):
#     def determin_version(self,request):
#         version = request.query_params.get('version')
#         return version
#

from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
# class UsersView(APIView):
#     versioning_class = QueryParameterVersioning
#     def get(self,request,*args,**kwargs):
#         print(request.version)
#         return HttpResponse('用户列表')

class UsersView(APIView):
    def get(self,request,*args,**kwargs):
        self.dispatch()
        # 1.获取版本
        print(request.version)
        # 2.获取版本的对象
        print(request.versioning_scheme)
        # 3. 内置的反向生成url，不需要指定版本，会自动生成，其实是当前url的版本
        u1 = request.versioning_scheme.reverse(viewname='uuu',request=request)
        print(u1)
        # 使用Django内置的反向生成url,必须要指定版本
        u2 = reverse(viewname='uuu',kwargs={'version':1})
        print(u2)
        return HttpResponse('用户列表')


class DjangoView(APIView):
    def get(self,request):
        print(type(request._request))
        from django.core.handlers.wsgi import WSGIRequest

        return HttpResponse('post 和body')


from rest_framework import request

class ParserView(APIView):
    # parser_classes = [JSONParser,FormParser]
    # JSONParser:表示只能解析content-type:application/json头
    #FormParser：表示只能解析content-type:application/x-www-form-urlencoded头
    def post(self,request,*args,**kwargs):
        """
        解析： 就是把请求体的内容转换成你可以看的格式
        允许用户发送JSON格式数据，可以接收json的那个头发来的数据，也可以接收字典格式的数据
        1，content-type:application/json
        2，{'name':'alex','age':18}
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        """
        只有用到的时候才会解析，这里使用到了data,所以由request.data触发
        解析：
        1.获取用户的请求
        2.获取用户的请求体
        3.根据用户请求头 和 parser_classes = [JSONParser,FormParser]中支持的请求头进行比较
        4.JSONParser符合，就是用JSONParser对象去请求体
        5.将解析的数据赋值给request.data
       """
        print(request.data)
        return HttpResponse('ParserView')



