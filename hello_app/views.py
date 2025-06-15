from django.http import JsonResponse, request
from django.shortcuts import render
from datetime import datetime as dt

from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView

from hello_app.models import Person


#-----------------------MESSAGES -----------------------
class BaseMessageView(View):
    message = "Mensagem padrão!"
    def get(self, request):
        return JsonResponse({"message":f'{self.message}!'})

class HelloWorldView(BaseMessageView):
    message = "Hello, World!"

class GoodbyeView(BaseMessageView):
    message = "Goodbye, see you next time!"

class TimeView(BaseMessageView):
    now = dt.now()
    time = now.strftime('%H:%M:%S')
    message = {
        "current_time": f"{time}"
    }

class GreetView(BaseMessageView):
    def get(self,request):
        name = request.GET.get('name', 'Stranger')
        self.message = f"Hello, {name}!"
        return super().get(request)

#----------------------------AGE-----------------------------------------
class AgeView(View):
    def get(self, request):
        if 'age' not in request.GET:
            return JsonResponse(
                {"error": "Missing 'age' parameter."},
                status=400
            )

        try:
            age = int(request.GET.get('age'))
        except (TypeError, ValueError):
            return JsonResponse(
                {"error": "Missing 'age' parameter."},
                status=400
            )

        if age <0:
            return JsonResponse(
                {"error": "Missing 'age' parameter."},
                status=400
            )
        elif 0 <= age <= 12:
            age_category = "Child"
        elif 13 <= age <= 17:
            age_category = "Teenager"
        elif 18 <= age <= 59:
            age_category = "Adult"
        else:
            age_category = "Senior"

        return JsonResponse({
            "category": age_category
        })

    # Rota Soma ----------------------------------------------------------
def sum_view(request, num1, num2):
    try:
        num1int = int(num1)
        num2int = int(num2)
    except ValueError:
        return JsonResponse(
            {"error": "Invalid input, please provide two integers."},
            status=400
        )

    total = num1int + num2int
    return JsonResponse({"sum": total})

    #---------------------------------HTML View---------------------------------------
class AboutView(TemplateView):
    template_name="hello_app/about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.GET.get('name','Visitante')
        context['ano'] = timezone.now().year
        return context

class PeopleView(View):
    def get(self, request):
        people = Person.objects.all()
        data = [{'name':p.name, 'age':p.age} for p in people]
        return JsonResponse({'people': data})