from dataclasses import field
from re import template
from django.forms import models
from django.shortcuts import render
from django.views.generic import ListView,DetailView, TemplateView
from .models import Mexanika, Molekulyar, Elektrostatika, Optika, AtomYadro, Muallif, Kitob, KunYangiliklar

# Create your views here.
class HomePageView(TemplateView):
    template_name='home.html'
class MexanikaListView(ListView):
    model=Mexanika
    template_name='mex.html'
class MexanikaDetailView(DetailView):
    model=Mexanika
    template_name='mex_detail.html'
class MolekulyarListView(ListView):
    model=Molekulyar
    template_name="molekulyar.html"
class MolekulyarDetailView(DetailView):
    model=Molekulyar
    template_name='molekulyar_detail.html'
class ElektrostatikaListView(ListView):
    model=Elektrostatika
    template_name='elektrostatika.html'
class ElektrostatikaDetailView(DetailView):
    model=Elektrostatika
    template_name='elektrostatika_detail.html'
class OptikaListView(ListView):
    model=Optika
    template_name='optika.html'
class OptikaDetailView(DetailView):
    model=Optika
    template_name='optika_detail.html'
class AtomYadroListView(ListView):
    model=AtomYadro
    template_name='atomyadro.html'
class AtomYadroDetailView(DetailView):
    model=AtomYadro
    template_name='atomyadro_detail.html'
class MuallifListView(ListView):
    model=Muallif
    template_name='muallif.html'
class KitobListView(ListView):
    model=Kitob
    template_name='kitob.html'
class KunYangiliklarListView(ListView):
    model=KunYangiliklar
    template_name='kunyangiliklar.html'
class KunYangiliklarDetailView(DetailView):
    model=KunYangiliklar
    template_name='kunyangiliklar_detail.html'
# class KunYangiliklarCreateView(CreateView):
#     model=KunYangiliklar
#     template_name='post_new.html'
#     fields=['title', 'body', 'author', 'rasm', 'time']

