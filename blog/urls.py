from django.urls import path
from .views import home_view, follow_unfollow, like, blog_search_view

urlpatterns = [
    path('', home_view),
    path('follow/', follow_unfollow),
    path('like/', like),
    path('search/', blog_search_view, name='blog_search_view'),
    # path('test_view/', test_sql)
]
