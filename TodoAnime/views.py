from django.shortcuts import render
from TodoAnime.models import Otaku, Perfil
from TodoAnime.forms import OtakuForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, 'TodoAnime/index.html')

class OtakuList(ListView):
    model = Otaku
    context_object_name = 'otakus'
    
class OtakuMineList(LoginRequiredMixin, OtakuList):
    
    def get_queryset(self):
        return Otaku.objects.filter(publisher=self.request.user.id).all()

        
class OtakuDetail(DetailView):
    model = Otaku
    context_object_name = 'otaku'
    
class PermissionOnlyOwner(UserPassesTestMixin):
    def test_func(self):
        user_id = self.request.user.id
        otaku_id = self.kwargs.get("pk")
        return Otaku.objects.filter(publisher=user_id, id= otaku_id).exists()
    
class OtakuUpdate(LoginRequiredMixin, PermissionOnlyOwner, UpdateView):
    model = Otaku
    success_url = reverse_lazy('otaku-list')
    fields = '__all__'
    
class OtakuDelete(LoginRequiredMixin, PermissionOnlyOwner, DeleteView):
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
    
class PerfilCreate(CreateView):
    model = Perfil
    success_url = reverse_lazy('otaku-list')
    fields = ['avatar']
    
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    
class PerfilUpDate(UserPassesTestMixin, UpdateView):
    model = Perfil
    success_url = reverse_lazy('otaku-list')
    fields = ['avatar']
    
    def test_func(self):
        return Perfil.objects.filter(user=self.request.user).exists()