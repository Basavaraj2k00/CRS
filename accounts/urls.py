from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import handler404, handler500, handler403, handler400


handler404 = views.error_404
handler500 = views.error_500


urlpatterns = [
    path("login", views.login_page, name="login"),
    path("register", views.register_page, name="register"),
    path("logout", views.logout_page, name="logout"),

    path("dashboard", views.dashboard_page, name="dashboard"),
    
    path("profile", views.account_settings, name="profile"),
    path("add_listing", views.add_listing, name="add_listing"),
    path("owner_dashboard", views.owner_dashboard, name="owner_dashboard"),






    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),name="password_reset_complete"),




]