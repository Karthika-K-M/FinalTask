from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
#from newtrproject import static

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('edit_user', views.edit_user, name='edit_user'),
]