from django.urls import path
from main import views

urlpatterns=[
    path('',views.index,name='index'),
    path('article/<int:pk>',views.article,name='get_article'),
    path('article',views.create_article,name='create_article')
]