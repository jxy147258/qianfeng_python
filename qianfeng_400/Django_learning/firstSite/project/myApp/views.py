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


def students2(request):
    # 先去模板里取数据
    studentsList = Students.stuObj.get(sgender=True)
    # 将数据传递给模板，模板再渲染页面，将渲染 好的页面返回给浏览器
    # return render(request, "myApp/students.html", {"students": studentsList})
    return HttpResponse("----------")


# 限制显示前几条数据
def students3(request):
    # 先去模板里取数据
    studentsList = Students.stuObj.all()[0:3]
    return render(request, "myApp/students.html", {"students": studentsList})


# 分页功能
def stupage(request, page):
    # 先去模板里取数据
    # 第1页，显示0-5,第2页显示5-10,第3页显示10-15
    page = int(page)
    studentsList = Students.stuObj.all()[page * 5 - 5:page * 5]
    return render(request, "myApp/students.html", {"students": studentsList})
    # return HttpResponse("----------")


def studentSearch(request):
    # 字段查询实例：contain
    # studentList = Students.stuObj1.filter(sname__contains="zhang")
    # 字段查询实例：startswith
    studentList = Students.stuObj1.filter(sname__startswith="li")
    return render(request, "myApp/students.html", {"students": studentList})


def gradesStudents(request, num):
    # 按传入的班级id号去取所有学生信息
    grade = Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    # 返回给模板
    return render(request, "myApp/students.html", {"students": studentsList})


from django.db.models import F, Q


# F对象的使用示例
def gradesF(request):
    # F对象的使用，拿出女孩人数多于男孩人数的班级
    # gradesList = Grades.objects.filter(ggirlnum__lt=F("gboynum"))
    # Q对象的使用，拿出pk值小于等于14,或者sage大于等于15的学生
    studentList = Students.stuObj1.filter(Q(pk__lte=14) | Q(sage__gt=50))
    # F对象还可以做加减等算术运算
    # gradesList = Grades.objects.filter(ggirlnum__lt=F("gboynum")-50)
    print(studentList)
    # 返回给模板
    return HttpResponse('0000000000')
    # return render(request, "myApp/grades.html", {"grades": gradesList})


def addstudents(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("qitiandasheng", 34, True, "wo shi qitiandasheng", grade)
    stu.save()
    return HttpResponse("%s-保存成功" % stu.sname)


def kuabiao(request):
    g = Grades.objects.filter(students__scontend__contains="zhang")
    return render(request, "myApp/grades.html", {"grades": g})
