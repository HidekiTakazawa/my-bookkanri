from django.urls import path
from . import views
#app_name = 'bookkanri'
urlpatterns = [
    path('', views.index, name='index'),
    path('bookNew/', views.bookNew, name='bookNew'),
    path('<int:bookdata_id>/bookUpdate/', views.bookUpdate, name='bookUpdate'),
    path('<int:bookdata_id>/bookDelete/', views.bookDelete, name='bookDelete'),
    #path('<int:bookdata_id>/bookRead/', views.bookRead, name='bookRead'),
    
]