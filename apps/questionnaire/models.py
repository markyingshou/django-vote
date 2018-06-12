from datetime import datetime

from django.db import models


# Create your models here.
from utils.ImageStorage import ImageStorage


class SurveyCategory(models.Model):
    """
    问卷类型
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name=u"类别名", help_text="类别名")
    cat_desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat")
    is_tab = models.IntegerField(choices=((0,"非导航"),(1,"导航")),default=0, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "问卷类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SurveyItem(models.Model):
    """
    问卷的问题
    """
    title = models.CharField(max_length=30, null=False, blank=False, verbose_name="问卷标题")
    category = models.ForeignKey(SurveyCategory, verbose_name=u"问卷类目")
    survey_desc = models.TextField(null=False, blank=False, verbose_name=u"问卷的描述")
    add_time = models.DateTimeField(default=datetime.now, max_length=6, verbose_name=u"添加时间")
    front_image = models.ImageField(upload_to="survey/images/%Y/%m/%d/",storage=ImageStorage(), null=True, blank=True, verbose_name=u"封面图")
    is_new = models.BooleanField(default=False, verbose_name=u"是否新的调查")
    is_hot = models.BooleanField(default=False, verbose_name=u"是否热门调查")

    class Meta:
        verbose_name = "调查问卷"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class SurveyTitle(models.Model):
    """
    每套选择题的题目
    """
    SURVEY_TYPE = (
        ("text", "输入文本"),
        ("radio", "单选"),
        ("checkbox", "多选"),
    )
    survey = models.ForeignKey(SurveyItem, verbose_name=u"调查的问卷", related_name="titles")
    if_require = models.IntegerField(choices=((0, "非必填"), (1, '必填')), default=0, verbose_name=u"是否必填", blank=False)
    title = models.CharField(max_length=50,blank=False,null=False,verbose_name=u"题目标题")
    tips = models.CharField(max_length=60,blank=True,null=False,default='',verbose_name=u"题目提示")
    index_by = models.IntegerField(default=0,verbose_name=u"排序")
    survey_type = models.CharField(max_length=100,choices=SURVEY_TYPE,default="radio",verbose_name=u"选择题类型")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = '问卷题目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class TitleChoice(models.Model):
    """
    题目的选项
    """
    IF_EXTRA = (
        (0, "不填其它"),
        (1, "填其它"),
    )
    surveyTitle = models.ForeignKey(SurveyTitle, verbose_name=u"题目的选项", related_name="choices")
    title = models.CharField(max_length=50,blank=False,null=False,verbose_name=u"题目标题")
    choice_val = models.CharField(max_length=255,default="",blank=False,null=False,verbose_name=u"题目的值")
    index_by = models.IntegerField(default=0,verbose_name=u"排序")
    if_extra = models.IntegerField(default=0,choices=IF_EXTRA,verbose_name=u"是否填写其它")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = '题目选项'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.title

class ChoiceAnswer(models.Model):
    """
    用户选择的答案
    """
    survey = models.ForeignKey(SurveyItem, verbose_name=u"问卷")
    surveyTitle = models.ForeignKey(SurveyTitle, verbose_name=u"题目id")
    choice_val = models.CharField(max_length=255,default="",blank=False,null=False,verbose_name=u"题目的值")
    ip = models.GenericIPAddressField(default='0.0.0.0',verbose_name=u"ip地址")
    extra_text = models.CharField(max_length=200,default='',verbose_name=u"是否填写其它")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = '问卷答案'
        verbose_name_plural = verbose_name
        unique_together=(("ip","survey","surveyTitle"))

    def __str__(self):
        return self.survey.title

class AnswerStatic(models.Model):
    """
    统计记录表
    """
    survey_id = models.IntegerField(default=0, verbose_name=u"问卷")
    title_id = models.IntegerField(default=0, verbose_name=u"题目id")
    choice_val = models.CharField(max_length=255, default="", blank=False, null=False, verbose_name=u"题目的值")
    nums = models.IntegerField(default=0,blank=False,null=False,verbose_name=u"人数")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"生成统计时间")

    class Meta:
        verbose_name = u'统计表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.survey.title
