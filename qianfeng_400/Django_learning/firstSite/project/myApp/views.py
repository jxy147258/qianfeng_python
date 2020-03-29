from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpRequest
from .models import Grades
from .models import Students
from django.db.models import F, Q
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
# 定义了一个视图，也就是一个html页面,这是不用模板
# def index(request):
#     return HttpResponse("sunck is a good man !")
# 定义一个视图，使用模板
def index(request):
    return render(request, "myApp/index.html")


def detail1(request, num):
    return HttpResponse("detail-%s" % num)


def detail2(request, num, num2):
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


def attributions(request):
    print(request.path)
    print(request.FILES)
    # print(request.GET)
    print(request.method)
    print(request.POST)
    print(request.session)
    print(request.encoding)
    return HttpResponse("attributions")


# 获取get方法传递的参数
def get1(request):
    a = request.Get.get("a")
    b = request.Get.get("b")
    c = request.Get.get("c")


def get2(request):
    a = request.Get.getlist("a")


def showregist(request):
    return render(request, "myApp/regist.html")


def regist(request):
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    hobby = request.POST.getlist("hobby")
    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse("0000")


def showresponse(request):
    res = HttpResponse()
    res.content = b"sunck is a good man!"
    print(res.content)
    print(res.charset)
    print(res.status_code)
    # print(res.content-type)
    return HttpResponse("0000")


def cookietest(request):
    res = HttpResponse()

    # F12中可以查看到Response响应头中的set-cookie的value是sunck=good
    # cookie = res.set_cookie("sunck", "good")
    # 有了上面的设置，以后的请求中cookie都带有此值，以下的语句取出cookie值
    cookie = request.COOKIES
    res.write("<h1>"+cookie["sunck"]+"</h1>")
    return res



def redirect1(request):
    # 如果重定向的url前面没有/，就是在前一个url的基础上在后面直接加重定向的url，
    # return HttpResponseRedirect("redirect2")就是形成/redirect1/redirect2,
    # 如果加了/，就是写什么url就跳转到该url
    # 此例子是为了从127.0.0.1:80000/sunck/redirct1，跳转到/sunck/redirect2,所以为了正常匹配，
    # 应该写成/sunck/redirect2
    # 使用HttpResponseRedirect重定向
    # return HttpResponseRedirect("/sunck/redirect2/")
    # 使用redirect重定向
    return redirect("/sunck/redirect2/")


def redirect2(request):
    return HttpResponse("我是重定向的视图")


def main(request):
    username = request.session.get("name", default="游客")
    print(username)
    return render(request, "myApp/main.html", {"username": username})


def login(request):
    return render(request, "myApp/login.html")


def showmain(request):
    username = request.GET.get("uname")
    request.session["name"] = username
    request.session.set_expiry(10)
    return redirect("/sunck/main")


from django.contrib.auth import logout
def quit(request):
    # logout(request)
    # request.session.clear()
    request.session.flush()
    return redirect("/sunck/main")
