PUT IN APP URLS
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    
]

____________________________________________________________________________________
PUT IN PROJECT URLS
from django.urls import path, include

urlpatterns = [
    path('', include('YOURAPPNAME.urls')),
]

___________________________________________________________________________________
PUT IN YOUR VIEWS
from django.shortcuts import render, HttpResponse, redirect
from .models import User    <---------   For importing classes

def index(request):
    
    context = {
        "all_users": User.objects.all()
    }
    
    return render(request, "index.html", context)  <------ context if needed

____________________________________________________________________________________

ADD "templates" folder.
ADD "static" folder.
____________________________________________________________________________________
TO LOAD CSS
 {% load static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
____________________________________________________________________________________
FOR FORMS
 {% csrf_token %}
 ___________________________________________________________________________________
SAMPLE FOR LOOP

 {% for user in all_users %}
<td>{{user.first_name}}</td>
<td>{{user.last_name}}</td>
<td>{{user.age}}</td>
<td>{{user.email_address}}</td>
<td>{{user.created_at}}</td>
    {% endfor %}
    
--------------------------------------------------------------------------------------

ADD STATIC FOLDER TO ROOT AND THIS CODE POINTS TO IT.  LOOKS IN BASE/ROOT DIR FOR 'STATIC' FOLDER

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

USING JINJA TO POINT TO FILE. CAN BE USED FOR IMAGES AND URLS AS WELL

href="{% static 'css/main.css' %}"
