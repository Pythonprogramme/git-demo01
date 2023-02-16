from django.urls import path
# 引入当前app的viws
from apps.orderweb.views import complete,finance,warehouse,service
# 匹配当前app中的url
urlpatterns = [
    # 全部信息
    path('complete/', complete.index, name="complete"),
    path('complete/list/', complete.list_values, name="list_complete"),# http://127.0.0.1:8000/order/complete/list/
    path('complete/order_number/exists', complete.is_order_number_exists, name="is_order_number_exists"),
    path('complete/add/', complete.add_value, name="add_complete"),


    # 财务信息
    path('finance/', finance.index, name="finance"),
    path('finance/list/', finance.list_values, name="list_finance"),
    # 仓库信息
    path('warehouse/', warehouse.index, name="warehouse"),
    path('warehouse/list/', warehouse.list_values, name="list_warehouse"),
    # 客服信息
    path('service/', service.index, name="service"),
    path('service/list/', service.list_values, name="list_service")
]