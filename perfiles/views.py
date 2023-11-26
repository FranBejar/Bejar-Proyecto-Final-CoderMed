from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from perfiles.forms import UserRegisterForm, CustomAuthenticationForm

def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('login')
            return redirect(url_exitosa)
    else:
        formulario = UserRegisterForm()
    
    return render(
        request=request,
        template_name='perfiles/registro.html',
        context={'form':formulario},
    )

def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('index')
                return redirect(url_exitosa)
    else:
        form = CustomAuthenticationForm()
    return render (
        request=request,
        template_name="perfiles/login.html",
        context={'form': form}
    )

class CustomLogoutView(LoginRequiredMixin,LogoutView):
    template_name = "perfiles/logout.html"

def usuarios(request):
    contexto={}
    http_response = render(
        request=request,
        template_name='perfiles/usuarios.html',
        context=contexto
    )
    return http_response
