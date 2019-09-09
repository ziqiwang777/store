from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length = 20,verbose_name = "姓名")
    phone = models.CharField(verbose_name = "电话",max_length = 14)
    personal_info = models.CharField(max_length = 100,verbose_name = "职位或者公司名称")
    message_c = models.CharField(max_length = 200,verbose_name = "留言信息")
    publish=models.DateTimeField()

    class Meta:
        verbose_name = "留言信息"
        verbose_name_plural = verbose_name
        db_table = "message"

    def __str__(self):
        return self.name
