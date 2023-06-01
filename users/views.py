from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser, Details, Profit_loss

# Create your views here.
import random
from datetime import date, datetime, timedelta

class AdminPageView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'details'
    model = Details
    login_url = 'account_login'

def admin(request):
    details = Details.objects.all()
    return render(request, 'index.html', {'details': details})

class UserPageView(LoginRequiredMixin ,TemplateView):
    template_name = 'user-dashboard.html'
    login_url = 'account_login'

datenow = datetime.now()
date1_min = datenow + timedelta(minutes=1)

def chart_view(request):
    labels = [datenow for i in range(50)]
    data = [random.uniform(-30, 75) for i in range(50)]

    chart_data = {
        'labels': labels,
        'data': data,
    }
    return JsonResponse(chart_data)