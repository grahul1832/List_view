from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from app.models import *


class Template_list(ListView):
    model=Trainer
    template_name='Template_list.html'
    context_object_name='tl'
    #queryset=Trainer.objects.filter(t_name='binny')
    ordering = ['t_name']

