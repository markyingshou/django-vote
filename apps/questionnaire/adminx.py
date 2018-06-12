#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import SurveyItem, SurveyTitle, SurveyCategory, TitleChoice, ChoiceAnswer, AnswerStatic


class SurveyItemAdmin(object):
    list_display = ["title", "category", "add_time", "front_image", "is_new", "is_hot"]
    search_fields = ["title", "is_new", "is_hot"]
    list_editable = ["is_hot", "is_new"]
    list_filter = ["is_hot", "is_new", "category", "add_time"]

    class SurveyTitleInline(object):
        model = SurveyTitle
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [SurveyTitleInline]


class SurveyTitleAdmin(object):
    list_display = ["survey", "if_require", "tips", "title", "survey_type", "add_time"]
    list_filter = ["if_require", "survey_type", "add_time"]
    search_fields = ['title']


class SurveyCategoryAdmin(object):
    list_display = ["name", "cat_desc", "category_type", "add_time", "is_tab"]
    list_filter = ["name", "category_type", "add_time", "is_tab"]
    search_fields = ['cat_desc', ]


class TitleChoiceAdmin(object):
    list_display = ["surveyTitle", "title", "choice_val", "index_by", "if_extra", "add_time"]
    list_filter = ["if_extra", "add_time"]
    search_fields = ['title', ]


class ChoiceAnswerAdmin(object):
    list_display = ["survey", "surveyTitle", "choice_val", "ip", "extra_text", "add_time"]
    list_filter = ["survey", "surveyTitle"]
    search_fields = ['surveyTitle', "ip"]

class AnswerStaticAdmin(object):
    data_charts = {
        "survey_count": {'title': u"调查问卷统计", "x-field": "title_id", "y-field": ("nums"),
                       "order": ('title_idpi',)},
    }


xadmin.site.register(AnswerStatic, AnswerStaticAdmin)
xadmin.site.register(ChoiceAnswer, ChoiceAnswerAdmin)

xadmin.site.register(SurveyCategory, SurveyCategoryAdmin)
xadmin.site.register(SurveyItem, SurveyItemAdmin)
xadmin.site.register(SurveyTitle, SurveyTitleAdmin)
xadmin.site.register(TitleChoice, TitleChoiceAdmin)
