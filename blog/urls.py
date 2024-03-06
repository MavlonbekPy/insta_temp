from django.urls import path
from .views import home_view, follow

urlpatterns = [
    path('', home_view),
    path('follow/', follow)
]
