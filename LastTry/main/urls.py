from django.urls import path, register_converter
from .classurl import FourDigitYearConverter
from . import views


register_converter(FourDigitYearConverter, "yyyy")
urlpatterns = [
    path('', views.index, name='homepage'),
    path('about', views.about,name='about'),
    path('Student/<int:studentID>/', views.StudentList, name='Students'),
    path('year/', views.years_mainpage, name='yearsHomepage'),
    path('year/<yyyy:year_id>/', views.year, name='year'),
    path('err400/', views.err400),
    path('err500/', views.err500),
]
