
from django.contrib import admin
from django.urls import path,include
from main.views import index, pageNotFound, Forbidden, ErrBadRequest, InternalServerError

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
handler404 = pageNotFound
handler403 = Forbidden
handler400 = ErrBadRequest
handler500 = InternalServerError