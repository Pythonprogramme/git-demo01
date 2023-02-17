from django.db import models
from basicweb.models import company,position

# 订单的类
class Order(models.Model):
    order_number = models.CharField(verbose_name="订单编号", primary_key=True, max_length=100)
    sj_name = models.CharField(verbose_name="收件姓名", max_length=100)
    sj_mobile = models.CharField(verbose_name="收件电话", max_length=100)
    order_date = models.DateField(verbose_name="订单日期")
    sj_address = models.CharField(verbose_name="收件地址", max_length=500)
    product_name = models.CharField(verbose_name="商品名称",max_length=250)
    price = models.FloatField(verbose_name="价格")
    payment_method = models.CharField(verbose_name="付款方式", max_length=100)
    jf_date = models.DateField(verbose_name="进粉日期")
    jz_name = models.CharField(verbose_name="金主姓名", max_length=100)
    remarks = models.CharField(verbose_name="八字/供灯/排位/发会/财库", max_length=500)
    write_state = models.CharField(verbose_name="书写状态",max_length=100,choices=(('已书写','已书写'),('未书写','未书写')))
    kg_date = models.DateField(verbose_name="开光日期")
    sy_remark = models.CharField(verbose_name="寺院备注",max_length=500)
    fh_remark = models.CharField(verbose_name="发货备注", max_length=500)
    service_name = models.CharField(verbose_name="客服姓名", max_length=100)
    # 关联到部门
    company = models.ForeignKey(verbose_name="部门",to=company,on_delete=models.PROTECT)
    # 关联到岗位
    position = models.ForeignKey(verbose_name="岗位",to=position,on_delete=models.PROTECT)
    fh_data = models.DateField(verbose_name="发货日期")
    courier_number = models.CharField(verbose_name="快递单号",max_length=100)
    shipping_status = models.CharField(verbose_name="发货状态", max_length=100, choices=(('已发货', '已发货'), ('未发货', '未发货')),default="未发货")
    number = models.IntegerField(verbose_name="数量")
    else_one = models.CharField(verbose_name="其他1", max_length=100)
    else_two = models.CharField(verbose_name="其他2", max_length=250)
    else_three = models.CharField(verbose_name="其他3", max_length=500)

    class Meta:
        managed = True
        app_label = 'orderweb'
        db_table = 'jzt_data'
        verbose_name = 'Order'
        verbose_name_plural = 'Order'

    def __str__(self):
        return "%s" % self.sj_name
