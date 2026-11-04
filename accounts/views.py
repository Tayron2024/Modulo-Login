"""Vistas del módulo de autenticación."""
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET

from .forms import RegistroForm


def home(request):
    """Vista de inicio del módulo de login."""
    return render(request, 'accounts/home.html')


def registro(request):
    """Vista de registro de nuevos usuarios (con reCAPTCHA)."""
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = RegistroForm()
    return render(request, 'accounts/registro.html', {'form': form})


@require_GET
def health(request):
    """Health check para RNF02 (disponibilidad)"""
    return JsonResponse({'ok': True})
