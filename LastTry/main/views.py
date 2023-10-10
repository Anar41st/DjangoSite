from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden, HttpResponseServerError, HttpResponseBadRequest
from django.core.exceptions import PermissionDenied, BadRequest

def index(request):
    return HttpResponse("<h4>Проверка работы</h4>")
def StudentList(request,studentID):
    StudentsDict = {1: '1) Буренок Дмитрий 14.01.2005', 2: '2) Горбанёв Кирилл 25.01.2006',
                    3: '3) Капшукова Дарья 27.06.2004',
                    4: '4) Кашаева Раяна 27.06.2004', 5: '5) Климин Тимур 17.05.2004', 6: '6) Косенков Глеб 9.06.2004',
                    7: '7) Костин Максим 3.04.2001', 8: '8) Кузенков Богдан Н/Д', 9: '9) Миколадзе Антон 14.09.2004',
                    10: '10) Мишин Александр 21.08.2004', 11: '11) Мишин Алексей 21.08.2004',
                    12: '12) Пешеходько Арсений Н/Д',
                    13: '13) Сентюрина Екатерина 08.11.2002'}
    if 1 <= studentID <= 13:
        return HttpResponse(f"<h2>Студент</h2> <p>{StudentsDict[studentID]}</p>")
    else:
        return HttpResponse("<h1>Студент не найден</h1>")

def year(reguest, year_id):
    events = {2000: '<li> 2000</li>',
              2001: '<li> 2001</li>',
              2002: '<li> 2002</li>',
              2003: '<li> 2003</li>',
              2004: '<li> 2004</li>',
              2005: '<li> 2005</li>',
              2006: '<li> 2006</li>',
              2007: '<li> 2007</li>',
              2008: '<li> 2008</li>',
              2009: '<li> 2009</li>',
              2010: '<li> 2010</li>',
              2011: '<li> 2011</li>',
              2012: '<li> 2012</li>',
              2013: '<li> 2013</li>',
              2014: '<li> 2014</li>',
              2015: '<li> 2015</li>',
              2016: '<li> 2016</li>',
              2017: '<li> 2017</li>',
              2018: '<li> 2018</li>',
              2019: '<li> 2019</li>',
              2020: '<li> 2020</li>',
              2021: '<li> 2021</li>',
              2022: '<li> 2022</li>',
              2023: '<li> 2023</li>',
              }
    if 2000 <= int(year_id) <= 2023:
        return HttpResponse(f"<h1>Основные события {year_id} года</h1> <ul>{events[int(year_id)]}</ul>")
    else:
        return HttpResponse(f"<h1>{year_id} год отсутствует в списке</h1>")

def years_mainpage(request):
    if(request.GET):
        converted = str()
        for key in request.GET:
            converted += key + ": " + request.GET[key] + ", "
        return HttpResponse(f"<h2>Get-запрос</h2> <p>Содержание: {converted[:-2]}</p>")
    return HttpResponse("<h2>Главная страница years</h2> <p>Для вывода значимых событий года добавьте индекс в URL</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>404 страница не найдена</h1>')

def Forbidden(request, exception):
    return HttpResponseForbidden('<h1>403 forbidden</h1>')

def InternalServerError(request):
    return HttpResponseServerError('<h1>500 server error</h1>')

def ErrBadRequest(request, exception):
    return HttpResponseBadRequest('<h1>400 Bad request</h1>')
def err400(request):
    raise BadRequest
def err500(request):
    raise brbrbr