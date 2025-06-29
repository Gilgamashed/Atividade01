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

from personal_info_project import views
from personal_info_project.views import BaseMessageView, HelloWorldView, GoodbyeView, TimeView, GreetView, AgeView, \
    AboutView, \
    PeopleView, PeopleCreateView, PeopleGetView, PeopleDeleteView, PeopleUpdateView, FeedbackView, SuccessView, \
    PeopleGenderView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('hello/', HelloWorldView.as_view(), name='hello'),
    path('goodbye/', GoodbyeView.as_view(), name='goodbye'),
    path('time/', TimeView.as_view(), name='time'),
    path('greet/', GreetView.as_view(), name='greet'),

    path('age/', AgeView.as_view(), name='age'),

    path('sum/<str:num1>/<str:num2>/', views.sum_view, name='sum'),

    path('about', AboutView.as_view(), name='about'),

    path('person/', PeopleGenderView.as_view(), name='person_list'),                       #<---- Model:Person
    path("person/add", PeopleCreateView.as_view(), name='person_add'),
    path("person/detail/<int:person_id>", PeopleGetView.as_view(), name='person_detail'),
    path("person/delete/<int:person_id>", PeopleDeleteView.as_view(), name='person_delete'),
    path("person/edit/<int:person_id>", PeopleUpdateView.as_view(), name='person_edit'),

    path("feedback/", FeedbackView.as_view(), name='feedback' ),                     #<----- Manual form
    path("feedback/success", SuccessView.as_view(), name='feedback_success'),
]
