from django.urls import path
from .views import home_view, follow_unfollow, like, search_view, settings_view, profile_view
from . import views

urlpatterns = [
    path('', home_view),
    path('profile/', profile_view),
    path('follow/', follow_unfollow),
    path('like/', like),
    path('search/', search_view, name="search_view"),
    path('settings/', settings_view),
    path('image/<int:image_id>/', views.serve_image, name='serve_image'),
    # path('test_view/', test_sql)
]
