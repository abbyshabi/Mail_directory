from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^add',views.add,name = 'add'),
    url('^list',views.directory,name = 'list'),
]