from django.urls import path
from .views import home_view, follow, like, test_sql

urlpatterns = [
    path('', home_view),
    path('follow/', follow),
    path('like/', like),
    path('test_view', test_sql)
]
