from django.urls import path
from .views import home_view, follow_unfollow, like

urlpatterns = [
    path('', home_view),
    path('follow/', follow_unfollow),
    path('like/', like),
    # path('test_view/', test_sql)
]
