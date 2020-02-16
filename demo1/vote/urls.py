# author: WH
# date: 2020/2/16 19:12
from django.conf.urls import url
from . import views

app_name = 'vote'
urlpatterns = [
    url(r'^polls/$', views.index, name='polls'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^result/(\d+)/$', views.result, name='result'),
]
