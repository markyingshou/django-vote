# _*_ coding:utf-8 _*_
from django.db.models import Count
from django.forms import model_to_dict
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import SurveyCategory, SurveyItem, SurveyTitle, TitleChoice, ChoiceAnswer


class SurveyItemView(View):
    """
    调查问卷
    """

    def get(self, request, s_id):
        surveyItem = SurveyItem.objects.get(id=int(s_id))
        surveyTitles = surveyItem.titles.all().prefetch_related("choices")
        return render(request, 'survey/survey_item.html', {
            'surveyItem': surveyItem,
            "surveyTitles": surveyTitles,
            'surveyId': s_id
        })


class SurveyAddView(View):
    """
    添加投票记录
    """
    def post(self, request):
        AZ = ['A''B', 'C', 'D', 'E', 'F', 'G', 'H']
        surveyItem = SurveyItem.objects.filter(id=request.POST['survey']).first()
        ip = ''
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:  # 获取ip
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')

        if surveyItem is None:  # 不存在调查问卷那么就返回错误
            return HttpResponse('{"status":0,"msg":"不存在该调查问卷，请按正常流程填写问卷！"}', content_type="application/json")
        titles = surveyItem.titles.all()  # 问卷的所有题目
        titleIds = []
        for title in titles:
            titleIds.append(title.id)
        querysetlist = []
        for title, value in request.POST.items():  # 取整数的键才是题目的答案
            if (title.isdigit()):
                if int(title) not in titleIds:  # 如果文章没有该题目
                    return HttpResponse('{"status":0,"msg":"该问卷不存在该题目！"}', content_type="application/json")
                if len(request.POST.getlist(title)) == 1:
                    choiceVal = ''.join(request.POST.getlist(title))
                else:
                    choiceVal = '|'.join(request.POST.getlist(title))
                querysetlist.append(
                    ChoiceAnswer(choice_val=choiceVal, ip=ip, survey=surveyItem, surveyTitle_id=int(title)))
        try:
            ChoiceAnswer.objects.bulk_create(querysetlist)
        except Exception:
            return HttpResponse('{"status":1,"msg":"您好，该ip地址已经投票了！"}', content_type="application/json")
        return HttpResponse('{"status":1,"msg":"投票成功！"}', content_type="application/json")
