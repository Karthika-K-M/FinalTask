from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
#from newtrproject import static
app_name = 'finaltaskapp'
urlpatterns = [
    path('',views.demo,name='demo'),
    path('add/', views.add_movies, name='add_movies'),
    path('add_review/', views.add_review, name='add_review'),
    path('search_results/', views.search_results, name='search_results'),
    path('movie/<int:movie_id>/', views.details, name='details'),
    path('edit_movie/<int:id>/',views.edit_movie,name='edit_movie'),
    path('delete/<int:id>/',views.delete,name='delete'),
]

urlpatterns += staticfiles_urlpatterns()