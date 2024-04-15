from django.urls import path
from app.views import shortener_link, shortened_link


urlpatterns = [
    path('', shortener_link, ),
    path('', shortened_link, )
    ]
