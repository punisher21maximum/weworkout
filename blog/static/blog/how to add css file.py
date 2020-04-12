# how to add css file

step1 : where to store main.css
blog/
	static/
		blog/
			main.css 

step2 : write code in main.css 

step3 : how to load main.css file in base.html 

1)at top load static folder : {{load static}}

2)in head add main.css : 
    <link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}">

#main blog
#1 - get started with django
step1 : create new project
$ django-admin startproject weworkout // name of website
s2 : go to weworkout dir
$ cd weworkout
s3 : run website
$ python3.6 manage.py runserver
s4 : go to browser at localhost or 127.0.0.1
#2 get started with your webpage
s1 : create a new app
$ python3.6 manage.py startapp blog
s2 : include app in weworkout/settings.py 
INSTALLED_APPS = [
    'blog.apps.BlogConfig',
	...
]
s3 : create view in blog/views.py 

# start : 
step1 : 
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)

