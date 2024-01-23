from django.contrib import admin
from django.urls import path,include
from myapp import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/',include('myapp.urls')),
    path('', views.registration, name='registration'),
]

