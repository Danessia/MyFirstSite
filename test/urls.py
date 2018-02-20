from django.contrib.auth.views import login
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^quiz/$', login_required(views.quiz), name='quiz'),
    url(r'^clear/$', login_required(views.clear_view), name='clear'),
    url(r'^results/$', login_required(views.result_view), name='results'),

    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/signup/$', views.signup, name='login'),
]