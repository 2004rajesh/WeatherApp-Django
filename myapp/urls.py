from django.urls import path
from myapp import views

urlpatterns =[
    path('',views.home,name='Home'),
    path('delete/<CName>',views.delete_city,name="DCity"),
]