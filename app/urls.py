from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import SnippetListView, SnippetDetailView, SnippetUpdateView, SnippetDeleteView, ProfileListView, SnippetCreateView

urlpatterns = [
        path('', SnippetListView.as_view(), name='snippet-list'),
        path('<str:pk>', SnippetDetailView.as_view(), name='snippet-detail'),
        
        path('new/', SnippetCreateView.as_view(), name='snippet-create'),
        path('<str:pk>/update/', SnippetUpdateView.as_view(), name='snippet-update'),
        path('<str:pk>/delete/', SnippetDeleteView.as_view(), name='snippet-delete'),

        path('register/', views.register, name='register'),
        path('profile/', ProfileListView.as_view(), name='profile-list'),
        path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='app/logout.html'), name='logout'),
        
        path('health/', views.health, name='health'),
        path('statistics/', views.statistics, name='statistics'),
               ]
