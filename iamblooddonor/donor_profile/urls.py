from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

# All URLS For DonorProfileApp
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.donor_login, name='donor-login'),
    path('logout/', views.donor_logout, name='donor-logout'),
    path("add_donor/", views.add_donor, name='add-donor'),
    path("profile/", views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit-profile'),
    path('delete_profile/<int:id>/', views.delete_profile, name='delete-profile'),
    path('donor_list/<bgname>/', views.donor_list, name='donor-list'),
    path('donor_detail/<int:id>/', views.donor_detail, name='donor-detail'),
    path('bloodgroups/', views.bloodgroup, name='bloodgroup'),


    # Password reset views
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='donor_profile/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='donor_profile/password_reset_done.html'),
         name='password_reset_done'),
    path('password_confirm_reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='donor_profile/password_reset_cofirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='donor_profile/password_reset_complete.html'),
         name='password_reset_complete'),

    path('', include('django.contrib.auth.urls')),

]

