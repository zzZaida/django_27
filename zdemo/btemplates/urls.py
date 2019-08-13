
from django.conf.urls import url, include
from django.contrib import admin


from . import views


urlpatterns = [
    # 模板
    url(r'^template/$', views.TemplateView.as_view()),


]
