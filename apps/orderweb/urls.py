from django.urls import path
# 引入当前app的viws
from apps.orderweb.views import complete,finance,warehouse,service
# 匹配当前app中的url
urlpatterns = [
    # 全部信息
    path('complete/', complete.index, name="complete"),
    # 财务信息
    path('finance/', finance.index, name="finance"),
    # 仓库信息
    path('warehouse/', warehouse.index, name="warehouse"),
    # 仓库信息
    path('service/', service.index, name="service")
]