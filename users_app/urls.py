from django.urls import path
from users_app import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('register/',user_views.register,name='register'),
  path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
  path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
  path('password_reset',auth_views.PasswordResetView.as_view(template_name='templates/registration/password_reset_form.html'),name='password_reset'),
  path('password_reset_done',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
  path('password_reset_confirm',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
  path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete')
]
