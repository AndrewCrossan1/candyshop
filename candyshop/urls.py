from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from candyshop import settings

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path('admin/', admin.site.urls),
    # API endpoints
    path('api/v1/users/', include('users.urls', namespace='users')),
    path('api/v1/shop/', include('api.urls', namespace='shop')),
    # Core Utils (Password Reset, Email Verification)
    path('core/password-reset/', PasswordResetView.as_view()),
    path('core/password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^core/account-confirm-email/(?P<key>[-:\w]+)/$',
            VerifyEmailView.as_view(), name='account_confirm_email'),
    path('core/account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
]
# Add Static Files and Media Files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
