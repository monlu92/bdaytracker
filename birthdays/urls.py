from django.urls import path

from .views import BirthdayView

urlpatterns = [
    path('', BirthdayView.index, name='index'),
    path('birthdays/', BirthdayView.bday_list, name='birthdays'),
    path('new/', BirthdayView.new_bday, name='new_bday'),
    path('save_new/', BirthdayView.save_new, name='save_new'),
]