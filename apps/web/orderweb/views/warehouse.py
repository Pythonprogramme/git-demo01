# 引入基础模块
from resources_base.module_base.importmodules import *
# 引入数据类
from orderweb.models import Order


def index(request):
    return render(request, 'order/warehouse.html')

# 获取数据
def list_values(request):
    # 获取分页的page和limit
    page = int(request.POST.get('page',0))
    limit = int(request.POST.get('limit',0))
    q_str = request.POST.get('inputStr', '')

    # 获取全部信息
    objs = list(Order.objects.filter(Q(sj_name__icontains=q_str)|Q(product_name__icontains=q_str)|
                                     Q(order_number__icontains=q_str)|Q(shipping_status__icontains=q_str)).values('order_number','sj_name','sj_mobile','order_date',
    'sj_address','product_name','price','payment_method','jf_date','jz_name','remarks',
    'write_state','kg_date','sy_remark','fh_remark','service_name','fh_data',
    'courier_number','shipping_status','number'))
    # 定义一个返回的数据集
    res = {'code': 0, 'count': len(objs), 'data': objs}
    # 存储分页的数据变量
    one_page_data = ''
    # 判断是否收到 page和 limit
    if page !=0 and limit != 0:
        one_page_data = objs[(page-1)*limit:page * limit]
        res['data'] = one_page_data


    # 返回
    return JsonResponse(res)