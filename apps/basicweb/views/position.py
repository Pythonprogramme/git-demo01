from django.shortcuts import render,HttpResponse
# 引入 models类
from apps.basicweb.models import position
# 引入 json
from django.http import JsonResponse
def index(request):
    return render(request, 'basic/position.html')

# 获取模块
def list_value(request):
    # 数据分页
    # 获取传递过来的两个参数 page limit
    page = int(request.GET.get('page',0))
    limit = int(request.GET.get('limit',0))
    # 获取所有数据
    objs = list(position.objects.all().values('id','name','company__name'))
    # 获取当前页的数据
    obj_one_page = objs[(page - 1) * limit: page * limit]
    # 定义一个返回值类型 ---code状态、count分页、data返回一页的数据
    res = {'code':0,'count':len(objs), 'data':obj_one_page}
    # 返回数据
    return JsonResponse(res)
