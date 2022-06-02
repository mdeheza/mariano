from django.urls import path, include
from familiares.views import familiares1


urlpatterns = [
    path('',familiares1, name='familiares1'),
]