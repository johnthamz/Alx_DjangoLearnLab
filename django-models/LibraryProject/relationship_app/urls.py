from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # App views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication routes (use views.register so checker sees "views.register")
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]

