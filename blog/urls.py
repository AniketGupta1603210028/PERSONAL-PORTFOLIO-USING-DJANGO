
from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('',views.all_blogs,name='ALL_BLOGS'),
    path('<int:blog_id>/',views.details,name='DETAILS'),
]