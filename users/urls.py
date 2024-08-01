from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('profile/settings/', TemplateView.as_view(template_name='profile.html'), name='profile_settings'),
    path('profile/settings/basic/', TemplateView.as_view(template_name='profile.html'), name='profile_settings_basic'),
    path('profile/verification/', TemplateView.as_view(template_name='profile.html'), name='profile_verification'),
]
