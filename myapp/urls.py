from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.registration, name='registration'),
    path('success/',views.success,name='success'),
    path('user_exists/',views.user_exists,name='user_exists'),
    path('master',views.master,name='master'),
    path('display',views.display,name='display')
]