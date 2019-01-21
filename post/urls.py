from django.urls import path
from . import views
app_name = 'posts'

urlpatterns = [
     path('', views.index, name='index'),
     path('help/', views.help, name='help'),
     path('<int:post_id>/', views.detail ,name='detail'),
     path('<int:post>/update', views.update ,name='update'),
     path('create/', views.create ,name='create')

]
