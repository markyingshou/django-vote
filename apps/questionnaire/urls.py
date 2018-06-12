# _*_ coding:utf-8 _*_
__author__ = 'markyingshou'
__date__ = '2018/5/5 15:12'

from django.conf.urls import url,include
from .views import SurveyItemView,SurveyAddView

urlpatterns = [
    url(r'^detail/(?P<s_id>\d+)/$',SurveyItemView.as_view(),name='survey_detail'),
    url(r'^add/$', SurveyAddView.as_view(), name='survey_add'),

]