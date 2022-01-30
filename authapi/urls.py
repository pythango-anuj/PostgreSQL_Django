from django.urls import path, include
from . import views
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls'))
]