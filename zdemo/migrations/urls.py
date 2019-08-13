
from django.conf.urls import url, include
from django.contrib import admin


from . import views


urlpatterns = [
    # 模板
    url(r'^models/$', views.ModelsView.as_view()),


]
