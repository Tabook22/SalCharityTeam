from django.urls import path
from .views import addnew, plist,newcharity

app_name='ghelp'
urlpatterns = [
    path('', addnew),
    path('addnew/', addnew, name='addnew'),
    path('plist/', plist, name='plist'),
    path('newcharity/', newcharity, name="newcharity"),
]
