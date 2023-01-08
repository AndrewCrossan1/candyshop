from django.urls import path
from dj_rest_auth.registration.views import VerifyEmailView, RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from allauth.account.views import ConfirmEmailView
from rest_framework import routers

from .views import SingleUser, AllUsersView

app_name = 'users'

urlpatterns = [
    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view),
    path('registration/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),
    path('', AllUsersView.as_view(), name='user-list'),
    path('<int:id>/', SingleUser.as_view(), name='user-by-username')
]
