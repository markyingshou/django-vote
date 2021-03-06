# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-11 00:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='类别名', max_length=30, verbose_name='类别名')),
                ('cat_desc', models.TextField(default='', help_text='类别描述', verbose_name='类别描述')),
                ('category_type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], help_text='类目级别', verbose_name='类目级别')),
                ('is_tab', models.IntegerField(choices=[(0, '非导航'), (1, '导航')], default=0, help_text='是否导航', verbose_name='是否导航')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('parent_category', models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='questionnaire.SurveyCategory', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': '商品类别',
                'verbose_name_plural': '商品类别',
            },
        ),
        migrations.CreateModel(
            name='SurveyItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='问卷标题')),
                ('survey_desc', models.TextField(verbose_name='问卷的描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, max_length=6, verbose_name='添加时间')),
                ('front_image', models.ImageField(blank=True, null=True, upload_to='survey/images/', verbose_name='封面图')),
                ('is_new', models.BooleanField(default=False, verbose_name='是否新的调查')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热门调查')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.SurveyCategory', verbose_name='商品类目')),
            ],
            options={
                'verbose_name': '调查问卷',
                'verbose_name_plural': '调查问卷',
            },
        ),
        migrations.CreateModel(
            name='SurveyTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('if_require', models.IntegerField(choices=[(0, '非必填'), (1, '必填')], default=0, verbose_name='是否必填')),
                ('title', models.CharField(max_length=50, verbose_name='题目标题')),
                ('题目提示', models.CharField(blank=True, default='', max_length=60)),
                ('index_by', models.IntegerField(default=0, verbose_name='排序')),
                ('survey_type', models.CharField(choices=[('text', '输入文本'), ('radio', '单选'), ('checkbox', '多选')], default='radio', max_length=100, verbose_name='选择题类型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titles', to='questionnaire.SurveyItem', verbose_name='调查的问卷')),
            ],
            options={
                'verbose_name': '选择题目',
                'verbose_name_plural': '选择题目',
            },
        ),
        migrations.CreateModel(
            name='TitleChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='题目标题')),
                ('题目的值', models.CharField(max_length=255)),
                ('index_by', models.IntegerField(default=0, verbose_name='排序')),
                ('if_extra', models.IntegerField(choices=[(0, '不填其它'), (1, '填其它')], default=0, verbose_name='是否填写其它')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('surveyTitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='questionnaire.SurveyTitle', verbose_name='题目的选项')),
            ],
            options={
                'verbose_name': '选择题目',
                'verbose_name_plural': '选择题目',
            },
        ),
    ]
