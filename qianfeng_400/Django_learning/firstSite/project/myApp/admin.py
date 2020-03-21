from django.contrib import admin

# Register your models here.
from .models import Grades, Students


# in tabular 用表格形式呈现
class StudentsInfo(admin.TabularInline):  # 以竖排形式呈现 class StudentsInfo(admin.StackedInline):
    model = Students
    extra = 2


class GradeAdmin(admin.ModelAdmin):
    # 用于在年及标中
    inlines = [StudentsInfo]

    # 以下4个都是列表页的属性
    list_display = ["pk", "gname", "gdate", "ggirlnum", "gboynum", "isDelete"]
    # 添加一个过滤器，参数的含义是以哪个字段为过滤条件，可以是gname，也可以是gdate，ggirlnum，但是只能有一个过滤器
    list_filter = ["gname"]
    # 添加一个搜索框，参数含义是以哪个字段为查找条件
    search_fields = ["gname"]
    # 用于分页，参数是一页显示的条数
    list_per_page = 5

    # 以下2个是添加页、修改页都有的属性
    # 规定属性的的显示顺序，不会改变列表页的属性顺序
    # fields = ["ggirlnum", "gboynum", "gname", "gdate", "isDelete"]
    # 给属性分组，此属性和上一个属性不能同时使用
    fieldsets = [
        ("num", {"fields": ["ggirlnum", "gboynum"]}),
        ("base", {"fields": ["gname", "gdate", "isDelete"]})
    ]


admin.site.register(Grades, GradeAdmin)


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    # 把男女的True和False显示为男女
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    # 设置页面表头列的名称
    gender.short_description = "性别"

    actions_on_bottom = True
    actions_on_top = False

    list_display = ["pk", "sname", gender, "sage", "scontend", "sgrade", "isDelete"]
    list_per_page = 10


# admin.site.register(Students, StudentsAdmin)
