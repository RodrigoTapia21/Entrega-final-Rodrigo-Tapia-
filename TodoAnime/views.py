from django.shortcuts import render
from TodoAnime.models import Otaku
from TodoAnime.forms import OtakuForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'TodoAnime/index.html')

class OtakuList(ListView):
    model = Otaku
    context_object_name = 'otakus'
    
class OtakuDetail(DetailView):
    model = Otaku
    context_object_name = 'otaku'
    
class OtakuUpdate(LoginRequiredMixin, UpdateView):
    model = Otaku
    success_url = reverse_lazy('otaku-list')
    fields = '__all__'
    
class OtakuDelete(LoginRequiredMixin, DeleteView):
    model = Otaku
    success_url = reverse_lazy('otaku-list')
    context_object_name = 'otaku'
    
class OtakuCreate(LoginRequiredMixin, CreateView):
    model = Otaku
    success_url = reverse_lazy('otaku-list')
    fields = '__all__'
    
class OtakuSearch(ListView):
    model = Otaku
    context_object_name = 'otakus' 
    
    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        resultado = Otaku.objects.filter(Nombre_anime__icontains=criterio).all()
        return resultado

class Login(LoginView):
    next_page = reverse_lazy('otaku-list')
    
class SingUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('otaku-list')
    
class Logout(LogoutView):
    template_name = "registration/logout.html"