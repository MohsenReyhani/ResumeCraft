from django.urls import path, include
from .views import SettingView, login_view, logout_view, send_sms_code_view, verify_sms_code_view, lock
from django.contrib.auth import views


urlpatterns = [
    # Authentication
    # path('register/', views.register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('send-code/', send_sms_code_view, name='send_code'),
    path('verify-sms-code/', verify_sms_code_view, name='verify_sms_code'),
    # Settings App
    path('settings/', SettingView.as_view(), name="settings"),
#     path('password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
#     path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(
#         template_name='accounts/password-change-done.html'
#     ), name="password_change_done"),
#     path('password-reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
#     path('password-reset-confirm/<uidb64>/<token>/',
#         views.UserPasswrodResetConfirmView.as_view(), name="password_reset_confirm"
#     ),
#     path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
#         template_name='accounts/password-reset-done.html'
#     ), name='password_reset_done'),
#     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
#         template_name='accounts/password-reset-complete.html'
#   ), name='password_reset_complete'),

    path('lock/', lock, name="lock"),
]