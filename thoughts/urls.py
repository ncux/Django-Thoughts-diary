
from .views import thoughts, enter

from django.urls import path

app_name = 'thoughts'

urlpatterns = [
    path('thoughts', thoughts, name='thoughts'),
    path('enter', enter, name='enter')
]
