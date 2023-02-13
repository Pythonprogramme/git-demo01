from django.urls import path
# 引入当前app的viws
from apps.basicweb.views import company,position
# 匹配当前app中的url
urlpatterns = [
    #  公司管理
    path('company/',company.index, name="company"),
    path('company/list/',company.list_values, name="list_company"),
    path('company/add/',company.add_value, name="add_company"),
    path('company/edit/',company.edit_value, name="edit_company"),
    path('company/del/',company.del_value, name="del_company"),
    # 人员职位
    path('position/',position.index, name="position"),
    path('position/list/',position.list_value, name="list_position"),
    path('position/add/',position.add_value, name="add_position"),
    path('position/edit/',position.edit_value, name="edit_position"),
    path('position/del/',position.del_value, name="del_position")
]