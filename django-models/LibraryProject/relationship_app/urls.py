from django.urls import path 
from .views import list_books, LibraryDetailView, register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    # App views
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication routes
    path('accounts/register/', register_view, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
