# 引入基础模块
from resources_base.module_base.importmodules import *
# 引入数据类
# 引入 models类
from basicweb.models import position,company



def index(request):
    return render(request, 'basic/position.html')
# 获取模块
def list_value(request):
    # 数据分页
    # 获取传递过来的两个参数 page limit
    page = int(request.POST.get('page',0))
    limit = int(request.POST.get('limit',0))
    q_str = request.POST.get('inputStr','')
    # 获取所有数据
    objs = list(position.objects.filter(Q(name__icontains=q_str)|Q(Personal_name=q_str)|Q(company__name__icontains=q_str)).values('id','name','Personal_name','company__name','company_id'))
    # 获取当前页的数据
    obj_one_page = objs[(page - 1) * limit: page * limit]
    # 定义一个返回值类型 ---code状态、count分页、data返回一页的数据
    res = {'code':0,'count':len(objs), 'data':obj_one_page}
    # 返回数据
    return JsonResponse(res)
# 添加岗位
def add_value(request):
    # 获取传递过来的值
    company_val = request.POST.get('company')
    position_val = request.POST.get('position')
    position_name = request.POST.get('position_name')
    # 写入数据库
    try:
        position.objects.create(company_id=company_val,name=position_val,Personal_name=position_name)
        return JsonResponse({'status':True})
    except Exception as e:
        return JsonResponse({'status':False, 'error':'添加数据到数据库出现异常，具体原因：'+str(e)})
# 修改信息
def edit_value(request):
    # 获取传递过来的值
    rec = request.POST
    # 修改
    try:
        # 获取当前的操作对象
        obj = position.objects.filter(id=rec.get('position_id')).first()
        # 修改名称
        obj.name = rec.get('position')
        # 修改姓名
        obj.Personal_name = rec.get('position_name')
        # 修改部门
        obj.company = company.objects.filter(id=rec.get('company')).first()
        # 保存
        obj.save()
        # 返回
        return JsonResponse({'status':True})
    except Exception as e:
        return JsonResponse({'status':False, 'error':'修改数据到数据库出现异常，具体原因：'+str(e)})
# 删除信息
def del_value(request):
    # 接受传递的 id
    id = request.POST.get('id')
    # 实现删除的功能
    try:
        # 获取当前的操作对象
        position.objects.filter(id=id).first().delete()
        # 返回
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '删除数据提交到数据库出现异常，具体原因：' + str(e)})

