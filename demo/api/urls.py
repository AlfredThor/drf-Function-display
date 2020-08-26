from django.urls import re_path
from api import views

urlpatterns = [

    re_path(r'^index/$',views.Index.as_view(),name='index/'),

]