from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseServerError


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')


def custom_handler500(request, exception):
    return HttpResponseServerError('Ой, что то сломалось... Простите извините!')


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/index.html')


class DepartureView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/departure.html')


class TourView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/tour.html')
