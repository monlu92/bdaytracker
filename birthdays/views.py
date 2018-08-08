from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import Birthday
from .forms import BirthdayForm

# TODO: ability to delete a birthday
# TODO: list birthdays categorized by month
# TODO: ability to notify birthdays
# TODO: monthly view

class BirthdayView(TemplateView):

    def index(request):
        return render(request, 'birthdays/header.html', {})

    def bday_list(request):
        entries = Birthday.objects.all().order_by('bday_date')
        return render(request, 'birthdays/bday_list.html', {'entries': entries})

    def new_bday(request):
        form = BirthdayForm()
        return render(request, 'birthdays/bday_entry.html', {'form': form})

    def save_new(request):
        form = BirthdayForm(request.POST or None)
        if form.is_valid():
            form.save()
            context= {'form': form }
            return HttpResponseRedirect('/birthdays/')
        else:
            return render(request, 'birthdays/fail_save.html', {})

