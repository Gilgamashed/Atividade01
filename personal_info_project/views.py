from django.http import JsonResponse, request
from django.shortcuts import render
from datetime import datetime as dt

from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView, FormView

from personal_info_project.forms import PersonForm, FeedbackForm
from personal_info_project.models import Person


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
    template_name="personal_info_project/about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.GET.get('name','Visitante')
        context['ano'] = timezone.now().year
        return context

    #---------------------------------Person CRUD View---------------------------------------
class PeopleView(ListView):
    model = Person
    template_name = "personal_info_project/person_list.html"
    context_object_name = "people"

class PeopleCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = "personal_info_project/person_form.html"
    success_url = reverse_lazy('person_list')

class PeopleGetView(DetailView):
    model = Person
    template_name = "personal_info_project/person_detail.html"
    context_object_name = "person"
    pk_url_kwarg = "person_id"

class PeopleDeleteView(DeleteView):
    model = Person
    template_name = "personal_info_project/person_delete.html"
    pk_url_kwarg = "person_id"
    success_url = reverse_lazy("person_list")

class PeopleUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = "personal_info_project/person_form.html"
    pk_url_kwarg = "person_id"
    success_url = reverse_lazy("person_list")

#-------------------------------------------Manual Form-----------------------------------------------------
"""def feedback_view(request):
    form = FeedbackForm(request.POST or None)

    if form.is_valid():                         #valida se os campos foram preenchidos
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        rating = form.cleaned_data['rating']

        context = {"success": True, 'name':name}

        return render(request,'personal_info_project/feedback.html',context)
    return render(request,'personal_info_project/feedback.html', {'form':form})    #Se for GET ele cai aqui

"""

class FeedbackView(FormView):
    template_name = 'personal_info_project/feedback.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback_success')

class SuccessView(TemplateView):
    template_name = 'personal_info_project/feedback_success.html'

