from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Grades
from .models import Students


# 定义了一个视图，也就是一个html页面,这是不是用模板
# def index(request):
#     return HttpResponse("sunck is a good man !")
# 定义一个视图，使用模板
def index(request):
    return render(request, "myApp/index.html")


def detail(request, num, num2):
    return HttpResponse("detail-%s-%s" % (num, num2))


def grades(request):
    # 先去模板里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板，模板再渲染页面，将渲染 好的页面返回给浏览器
    return render(request, "myApp/grades.html", {"grades": gradesList})
    # 参数说明，"myApp/grades.html"是定义好的模板页面，
    # {"grades": gradesList})中的grades是模板中定义的变量，gradesList是视图中的变量


def students(request):
    # 先去模板里取数据
    studentsList = Students.stuObj.all()
    # 将数据传递给模板，模板再渲染页面，将渲染 好的页面返回给浏览器
    return render(request, "myApp/students.html", {"students": studentsList})


def gradesStudents(request, num):
    # 按传入的班级id号去取所有学生信息
    grade = Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    # 返回给模板
    return render(request, "myApp/students.html", {"students": studentsList})


def addstudents(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("qitiandasheng", 34, True, "wo shi qitiandasheng", grade)
    stu.save()
    return HttpResponse("%s-保存成功" % stu.sname)



