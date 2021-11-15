from django.urls import path,include
from .views import change_passwordview, loginview, logoutview, registerview,change_passwordview,homeview
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/',homeview,name='home'),
    path('login/',loginview,name='login'),
    path('home/logout/',logoutview,name='logout'),
    path('login/register/',registerview,name='register'),
    path('home/changep/',change_passwordview,name='changep'),
    path('login/password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')
]