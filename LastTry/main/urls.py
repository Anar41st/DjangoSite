from django.urls import path, register_converter
from .classurl import FourDigitYearConverter
from . import views


register_converter(FourDigitYearConverter, "yyyy")
urlpatterns = [
    path('', views.index),
    path('Student/<int:studentID>/', views.StudentList),
    path('YEAR/', views.years_mainpage),
    path('years/<yyyy:year_id>/', views.year),
    path('err400/', views.err400),
    path('err500/', views.err500),
]
