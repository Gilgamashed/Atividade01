from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime as dt


def welcome_view(request):
    response = {
        "message": "Welcome to the Personal Info API!"
    }
    return JsonResponse(response)

def goodbye_view(request):
    response = {
        "message": "Goodbye, see you next time!"
    }
    return JsonResponse(response)

def time_view(request):
    now = dt.now()
    time = now.strftime('%H:%M:%S')
    response = {
        "current_time": f"{time}"
    }
    return JsonResponse(response)

def greet_view(request):
    name = request.GET.get('name', 'Stranger')
    response = {
        "message": f"Hello, {name}!"
    }
    return JsonResponse(response)

#Rota Age -------------------------------------------------------
def age_view(request):
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

    if 0 <= age <= 12:
        age_category = "Child"
    elif 13 <= age <= 17:
        age_category = "Teenager"
    elif 18 <= age <= 59:
        age_category = "Adult"
    elif age >= 60:
        age_category = "Senior"
    else:
        return JsonResponse(
            {"error": "Missing 'age' parameter."},
            status=400
        )

    response = {
        "category": age_category
    }
    return JsonResponse(response)

#Rota Soma ----------------------------------------------------------
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