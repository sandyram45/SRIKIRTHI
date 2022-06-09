from django.urls import path
from .views import log_in, home, log_out


urlpatterns = [
    path('', log_in, name='login'),
    path('home/', home, name='home'),
    path('logout/', log_out, name='logout'),
]
