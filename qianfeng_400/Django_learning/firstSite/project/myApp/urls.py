from django.conf.urls import url
from . import views

urlpatterns = [
    # url中端口号8000的后面为空匹配此条
    url(r'^$', views.index, name="index"),
    # url中端口号8000的后面为index.html匹配此条
    url(r'index.html', views.index),


    # 为了验证url中/的位置，此条的完整url是，127.0.0.1:8000/a
    url(r'^a/', views.index),
    # url中端口号的后面是任意的数字匹配此条
    url(r"^(\d+)/$", views.detail1),
    # 关于正则的一个技巧，如果要显示100/200/这种样式，用两个括号
    url(r"^(\d+)/(\d+)/$", views.detail2),

    # 接受模板的传递，然后显示页面
    url(r"^grades/$", views.grades),

    # 接受模板的传递，然后显示页面
    url(r"^students/$", views.students),

    url(r"^grades/(\d+)/$", views.gradesStudents),

    # 用于在页面添加学生信息
    url(r"^addstudents/$", views.addstudents),

    # 为了演示get()方法中返回多个对象时会报如下的错：
    # myApp.models.Students.MultipleObjectsReturned: get() returned more than one Students -- it returned 6!
    url(r"^students2/$", views.students2),

    # 返回查询集的前5条
    url(r"^students3/$", views.students3),

    # 分页功能
    url(r"^stu/(\d+)$", views.stupage),

    # 带条件的查询功能
    url(r"^studentSearch/$", views.studentSearch),

    # F对象的使用示例
    url(r"^gradesF/$", views.gradesF),

    url(r"^kuabiao/$", views.kuabiao),



    # 视图函数讲解：
    # GET属性
    url(r"^attributions", views.attributions),

    # GET属性的两个方法，get(),getlist()
    url(r"^get1/$", views.get1),

    url(r"^get2/$", views.get2),
    # POST属性
    url(r"^showregist/$", views.showregist),
    url(r"^showregist/regist/$", views.regist),
    url(r"^showresponse/$", views.showresponse),

    # 测试cookie
    url(r"^cookietest/$", views.cookietest),

    # HttpResponseRedirect
    url(r"^redirect1/$", views.redirect1),
    url(r"^redirect2/$", views.redirect2),


    url(r"^main/$", views.main),
    url(r"^login/$", views.login),
    url(r"^showmain/$", views.showmain),
    url(r"^quit/$", views.quit),

]
