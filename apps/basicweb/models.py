from django.db import models

# 公司管理
class company(models.Model):
    name = models.CharField(verbose_name="部门名称",max_length=100,unique=True,null=False)

    class Meta:
        managed = True
        app_label = "basicweb"
        db_table = "Basic_company"
        verbose_name = "company"
        verbose_name_plural = "company"

    def __str__(self):
        return '%s' % self.name
# 人员职位
class position(models.Model):
    name = models.CharField(verbose_name="岗位名称",max_length=100,unique=True,null=False)
    company = models.ForeignKey(verbose_name="所属部门", to=company,on_delete=models.PROTECT)

    class Meta:
        managed = True
        app_label = "basicweb"
        db_table = "Basic_Major"
        verbose_name = "Major"
        verbose_name_plural = "Major"

    def __str__(self):
        return '%s' % self.name