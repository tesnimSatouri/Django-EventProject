
from django.urls import path
from . import views
urlpatterns = [
    path('Hello/<classe>',views.Hello)
    
]