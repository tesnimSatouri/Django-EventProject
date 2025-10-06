from django.urls import path
from django.contrib.auth.views import LogoutView ,LoginView
# 💡 Corrected/Added Import: Import the 'home' view
from .views import register, home 

urlpatterns=[
    path('register/', register, name='register'),
    path('Accueil/', home, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/',LoginView.as_view(), name='login'),  # Placeholder for login view
]