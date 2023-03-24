from django.shortcuts import render
from TodoAnime.models import Otaku
from TodoAnime.forms import OtakuForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def index(request):
    return render(request, 'TodoAnime/index.html')

class OtakuList(ListView):
    model = Otaku
    