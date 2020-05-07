from django.urls import path
from .views import addnew, plist,newcharity, newcharity2,fxtable

app_name='ghelp'
urlpatterns = [
    path('', addnew),
    path('addnew/', addnew, name='addnew'),
    path('plist/', plist, name='plist'),
    path('test/',fxtable),
    path('newcharity/', newcharity, name="newcharity"),
    path('newcharity2/', newcharity, name="newcharity2"),
]

