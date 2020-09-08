# -*- coding: utf-8 -*-
#!/usr/bin/env python
#================================================================
#   
#   
#   文件名称：urls.py
#   创 建 者：肖飞
#   创建日期：2020年09月08日 星期二 13时58分39秒
#   修改日期：2020年09月08日 星期二 15时02分15秒
#   描    述：
#
#================================================================
from django.conf.urls import url, include
from . import views
import sys

urlpatterns = [
    url(r'list$', views.list, ),
    url(r'csrf_token$', views.csrf_token, ),
]

def main(argv):
    pass

if '__main__' == __name__:
    main(sys.argv[1:])
