from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from candyshop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls', namespace='users')),
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
            VerifyEmailView.as_view(), name='account_confirm_email'),
    path('account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
