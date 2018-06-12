#!/usr/bin/env python
# encoding: utf-8

import xadmin
from xadmin import views

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "调查问卷系统"
    site_footer = "markyingshou"
    # menu_style = "accordion"


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
