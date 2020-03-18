from django.db import models

# Create your models here.
# 这里的一个class对应mysql中的一个数据库，每一个变量都是一个字段
class  Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return "%s-%d-%d" % (self.gname,self.ggirlnum,self.gboynum)

class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    # 此句关联外键
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)
