from django.db import models

# Create your models here.
#数据库类

class UserMessage(models.Model):  #数据库操作类

    object_id =models.CharField(max_length=50,primary_key=True,default='',verbose_name=u'主键')#设置id为主键 ， default:默认值
    name  = models.CharField(max_length=20,null=True,blank=True,default="",verbose_name=u"用户名")# 定义一个最大为20的字符串 ，用户名
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100,verbose_name=u"联系地址")
    message = models.CharField(max_length=500,verbose_name=u"留言信息")
    '''
    
        models.ForeignKey #外键类型
        models.EmailField#邮箱类型。
        models.DateTimeField#时间类型
        models.IntegerField#整型
        models.IPAddressField#IP地址类型
    '''


    class Meta:# 信息
        verbose_name =u"用户留言信息"
        verbose_name_plural = verbose_name
       # db_table ='user_message'  #生成的表名
        #ordering = "-object_id"#根据ID排序
