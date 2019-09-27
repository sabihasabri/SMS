from django.urls import path 
from .import views

from .import views 
app_name = 'polling'
urlpatterns = [

        path('', views.IndexView.as_view(), name='index'), 
        path('<int:pk>/results/', views.ResultsView.as_view(), name = 'results'),
        path('<int:pk>/', views.DetailView.as_view(), name='details'), 
        path ('<int:question_id>/vote/', views.vote, name='vote'), 

]
