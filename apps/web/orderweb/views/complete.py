# 引入基础模块
from resources_base.module_base.importmodules import *
# 引入数据类
from orderweb.models import Order


def index(request):
    return render(request, 'order/complete.html')

# 获取数据
def list_values(request):
    # 获取分页的page和limit
    page = int(request.POST.get('page',0))
    limit = int(request.POST.get('limit',0))

    q_str = request.POST.get('inputStr','')
    # 获取全部信息
    objs = list(Order.objects.filter(Q(sj_name__icontains=q_str)|Q(product_name__icontains=q_str)|
                                     Q(payment_method__icontains=q_str)|Q(jz_name__icontains=q_str)|
                                     Q(service_name__icontains=q_str)|Q(shipping_status__icontains=q_str)).values('order_number','sj_name','sj_mobile','order_date',
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

# 校验 订单编号是否存在
def is_order_number_exists(request):
    # 获取订单编号
    order_number = request.POST.get('order_number')
    # 判断
    is_exist = Order.objects.filter(order_number=order_number).exists()
    # 返回
    return JsonResponse({'data': is_exist})

# 添加订单数据
def add_value(request):
    # 接收传递的值
    rec = request.POST
    # 添加
    try:
        Order.objects.create(order_number=rec['order_number'],sj_name=rec['sj_name'],sj_mobile=rec['sj_mobile'],
                             order_date = rec['order_date'],sj_address = rec['sj_address'],product_name=rec['product_name'],
                             price = rec['price'],payment_method = rec['payment_method'],jf_date = rec['jf_date'],
                             jz_name = rec['jz_name'],remarks = rec['remarks'],write_state = rec['write_state'],
                             kg_date = rec['kg_date'],sy_remark = rec['sy_remark'],fh_remark = rec['fh_remark'],
                             service_name = rec['service_name'],fh_data=rec['fh_data'],courier_number = rec['courier_number'],
                             shipping_status = rec['shipping_status'],number = rec['number'])
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False,'error':'添加订单数据到数据库出现异常，具体原因：'+str(e)})

# 修改订单数据
def edit_value(request):
    # 接收传递的值
    rec = request.POST
    # 修改
    try:
        # 获取当前对象
        obj = Order.objects.get(order_number=rec['order_number'])
        # 逐一修改属性
        obj.sj_name = rec.get('sj_name')
        obj.sj_mobile = rec['sj_mobile']
        obj.order_date = rec['order_date']
        obj.sj_address = rec['sj_address']
        obj.product_name = rec['product_name']
        obj.price = rec['price']
        obj.payment_method = rec['payment_method']
        obj.jf_date = rec['jf_date']
        obj.jz_name = rec['jz_name']
        obj.remarks = rec['remarks']
        obj.write_state = rec['write_state']
        obj.kg_date = rec['kg_date']
        obj.sy_remark = rec['sy_remark']
        obj.fh_remark = rec['fh_remark']
        obj.service_name = rec['service_name']
        obj.fh_data = rec['fh_data']
        obj.courier_number = rec['courier_number']
        obj.shipping_status = rec['shipping_status']
        obj.number = rec['number']
        #  保存
        obj.save()
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '修改订单数据到数据库出现异常，具体原因：' + str(e)})

# 删除订单数据
def del_value(request):
    # 接收传递的值
    order_number = request.POST.get('order_number')
    # 修改
    try:
        # 获取当前对象
        Order.objects.get(order_number=order_number).delete()
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '删除订单数据到数据库出现异常，具体原因：' + str(e)})

