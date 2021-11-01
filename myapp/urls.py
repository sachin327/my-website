from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('index', views.index,name='index'),
    path('register', views.register,name='register'),
    path('login', views.loginPage,name='login'),
    path('logout', views.logoutPage,name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="myapp/password_reset_done.html"),name="password_reset_complete"),

]
