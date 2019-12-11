from app import views
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    url(r'^tasks/$', views.UserTaskList.as_view()),
    path('tasks/<int:pk>', views.UserTaskDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

