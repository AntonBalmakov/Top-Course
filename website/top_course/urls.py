from django.urls import path
from .views import index
from .views import other_page
from .views import shareholders
app_name = 'top_course'

urlpatterns = [

    path('<str:page>/', shareholders, name='shareholders'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),

]