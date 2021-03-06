from django.db import models

from apps.users.models import BaseModel
from DjangoUeditor.models import UEditorField

# Create your models here.
GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女")
)


class City(BaseModel):
    name = models.CharField(max_length=20, verbose_name=u"城市名")
    desc = models.CharField(max_length=200, verbose_name=u"描述")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(BaseModel):
    name = models.CharField(max_length=50, verbose_name="机构名称")
    desc = UEditorField(verbose_name="描述", width=600, height=300, imagePath="courses/ueditor/images/",
                          filePath="courses/ueditor/files/", default="")
    category = models.CharField(default="pxjg", verbose_name="机构类别", max_length=4,
                                choices=(("gx", "高校"), ("pxjg", "培训机构")))
    image = models.ImageField(upload_to="org/%Y/%M", verbose_name="logo", max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在城市")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

from apps.users.models import UserProfile
class Teacher(BaseModel):
    user = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="用户")
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构")
    name = models.CharField(max_length=50, verbose_name="教师名")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_position = models.CharField(max_length=50, verbose_name="职位")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=6, null=True)
    age = models.IntegerField(default=18, verbose_name="年龄")
    image = models.ImageField(upload_to="teacher/%Y/%M", verbose_name="头像", max_length=100)

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def course_nums(self):
        return self.course_set.all().count()