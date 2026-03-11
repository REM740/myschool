from django.urls import path, include
from . import views



app_name = 'highschool'

urlpatterns = [
    path('/', include('highschool.urls'))

]

