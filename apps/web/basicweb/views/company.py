# 引入基础模块
from resources_base.module_base.importmodules import *
# 引入数据类
# 引入数据库通用类
from resources_base.module_base import sqlhelper
# 导入类
from basicweb.models import company

def index(request):
    return render(request, 'basic/company.html')

def list_values(request):
    # 获取公司部门数据
    # 接受查询的条件
    q_str = request.POST.get('queryStr','')
    # 准备 sql语句
    sql = """
        SELECT T3.id,T3.name, COUNT(T3.id2) as 'number'
        FROM(SELECT T1.id, T1.name,T2.id AS "id2"
        FROM basic_company as T1 
        LEFT JOIN basic_major as T2 On T1.id = T2.company_id where T1.name like '%s') AS T3 
        GROUP BY T3.id,T3.name
    """ %('%' + q_str + '%')
    # 开始执行 sql语句
    response = sqlhelper.get_db_data_dict(sql, ['id', 'name', 'number'])
    # return HttpResponse(str(response))
    if response['status']:
        return JsonResponse({'status':True,'data': response['data']})
    else:
        return JsonResponse({'status':False,'error': response['error']})

    return JsonResponse(response)

# 添加部门信息
def add_value(request):
    # 接收传递过来的名称
    name = request.POST.get('name')
    try:
        # 写入数据库
        company.objects.create(name=name)
        # 返回
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False,'error':'写入数据库出现异常，具体原因:'+str(e)})

# 修改部门信息
def edit_value(request):
    # 获取传递过来的数据
    id = request.POST.get('id','')
    name = request.POST.get('name','')
    # 修改
    try:
        obj  = company.objects.get(id=id)
        obj.name = name
        obj.save()
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False,'error':'修改提交数据出现错误，具体原因:'+str(e)})

# 删除部门信息
def del_value(request):
    # 获取 id
    id = request.POST.get('id')
    # 删除
    try:
        company.objects.get(id=id).delete()
        return JsonResponse({'status':True})
    except Exception as e:
        return JsonResponse({'status':False,'error':'删除提交到数据库出现异常！具体原因:'+str(e)})