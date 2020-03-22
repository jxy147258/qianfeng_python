from django.db import models


# Create your models here.
# 这里的一个class对应mysql中的一张表，每一个变量都是一个字段
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    # def __str__(self):
    #     return "%s-%d-%d" % (self.gname,self.ggirlnum,self.gboynum)

    def __str__(self):
        return self.gname


# 重写管理器Manager类，作用是对于逻辑删除的不再显示出来
class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(isDelete=False)

    # 在自定义管理器中添加额外的方法
    def createStudent(self, name, age, gender, contend, grade, isD=False):
        stu = self.model()
        stu.sname=name
        stu.sage=age
        stu.sgender=gender
        stu.scontend=contend
        stu.sgrade=grade
        stu.isDelete=isD)
        return stu
该看312

class Students(models.Model):
    # 重写管理器，而且可以有多个管理器
    stuObj = StudentsManager()  # 使用这个管理器就会过滤掉isDelete=False的学生信息
    # stuObj1 = models.manager()  # 使用这个管理器就不会过滤
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    # 此句关联外键
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.sname

    #
    # class Meta:
    #     db_table = "students"
    #     ordering = ["id"]

    @classmethod  # 下面的cls就代表Students类
    def createStudent(cls, name, age, gender, contend, grade, isD=False):
        stu = cls(sname=name, sage=age, sgender=gender, scontend=contend, sgrade=grade, isDelete=isD)
        return stu
