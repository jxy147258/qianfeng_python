from django.conf.urls import url
from . import views

urlpatterns = [
    # url中端口号8000的后面为空匹配此条
    url(r'^$', views.index),
    # url中端口号的后面是任意的数字匹配此条
    # url(r"^(\d+)/$", views.detail),
    # 关于正则的一个技巧，如果要显示100/200/这种样式，
    url(r"^(\d+)/(\d)/$", views.detail),

    # 接受模板的传递，然后显示页面
    url(r"^grades/$", views.grades),

    # 接受模板的传递，然后显示页面
    url(r"^students/$", views.students),

    url(r"^grades/(\d+)/$", views.gradesStudents),

    # 用于在页面添加学生信息
    url(r"^addstudents/$", views.addstudents)

]
