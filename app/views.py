from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet
from .forms import UserRegistrationForm
from django.contrib import messages

def index(request):
    context = {
        'snippets': Snippet.objects.all()
    }
    return render(request, 'app/index.html', context)

def detail(request, pk):
    context = {
        'snippet': Snippet.objects.get(id=pk)
    }
    return render(request, 'app/detail.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('app:index')
    else:
        form = UserRegistrationForm()
    return render(request, 'app/register.html', {'form': form})

def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)
