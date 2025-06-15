"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from hello_app import views
from hello_app.views import BaseMessageView, HelloWorldView, GoodbyeView, TimeView, GreetView, AgeView, AboutView, \
    PeopleView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('hello/', HelloWorldView.as_view(), name='hello'),
    path('goodbye/', GoodbyeView.as_view(), name='goodbye'),
    path('time/', TimeView.as_view(), name='time'),
    path('greet/', GreetView.as_view(), name='greet'),
    path('age/', AgeView.as_view(), name='age'),
    path('about', AboutView.as_view(), name='about'),
    path('sum/<str:num1>/<str:num2>/', views.sum_view, name='sum'),
    path('people/', PeopleView.as_view(), name='people'),
]
