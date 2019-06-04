from .models import Snippet, User
from django.contrib import messages
from django.http import JsonResponse
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    context = {
        'snippets': Snippet.objects.all()
    }
    return render(request, 'app/index.html', context)

def detail(request, pk):
    context = {
        'snippets': Snippet.objects.all(),
        'snippet_detail': Snippet.objects.get(id=pk)
    }
    return render(request, 'app/detail.html', context)

@login_required
def profile(request):
    context = {
        'snippets': Snippet.objects.all(),
        'all_snippets': Snippet.objects.all().filter(owner=request.user.id)
    }
    return render(request, 'app/profile.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created ')
            return redirect('app:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'app/register.html', {'form': form})

def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)
