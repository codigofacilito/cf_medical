from django.urls import path

from .views import medicines
from .views import medicines_details

app_name = 'medicines'

urlpatterns = [
    path('/', medicines, name='medicines'),
    path('/<int:pk>', medicines_details, name='medicines_details'),
]
