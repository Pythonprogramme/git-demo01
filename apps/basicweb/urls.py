from django.urls import path
# 引入当前app的viws
from apps.basicweb.views import company,position
# 匹配当前app中的url
urlpatterns = [
    #  公司管理
    path('company/',company.index, name="company"),
    # 人员职位
    path('position/',position.index, name="position")
]