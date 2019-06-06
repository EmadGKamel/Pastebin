import csv
from django.http import HttpResponse
from app.models import Snippet, CustomUser
from app.helpers import get_pastes_num
from django.contrib import messages
from django.http import JsonResponse
from app.forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ProfileListView(LoginRequiredMixin, ListView):
    queryset = Snippet.objects.all().order_by('-creation_date')
    template_name = 'app/profile_list.html'
    context_object_name = 'snippets'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_snippets'] = Snippet.objects.all().filter(owner=self.request.user.id)
        return context

class SnippetListView(ListView):
    model = Snippet
    context_object_name = 'snippets'
    ordering = ['-creation_date']


class SnippetDetailView(DetailView):
    model = Snippet
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snippets'] = Snippet.objects.all().order_by('-creation_date')
        return context

class SnippetCreateView(LoginRequiredMixin, CreateView):
    model = Snippet
    fields = ['title', 'content', 'expiration_date', 'exposure_status']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class SnippetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Snippet
    fields = ['title', 'content', 'expiration_date', 'exposure_status']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Snippet = self.get_object()
        if self.request.user == Snippet.owner:
            return True
        return False

class SnippetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Snippet
    success_url = '/'

    def test_func(self):
        Snippet = self.get_object()
        if self.request.user == Snippet.owner:
            return True
        return False

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

def statistics(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="statistics.csv"'
    writer = csv.writer(response)

    writer.writerow(['username', 'snippets_number'])
    writer.writerows(get_pastes_num())
    return response

    

   