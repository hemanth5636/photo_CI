from django.urls import path, include
from .views import home_page, response_page

urlpatterns = [
    path('homePage/',home_page),
    path('response/', response_page)
]
