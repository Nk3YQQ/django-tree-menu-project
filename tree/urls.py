from django.urls import path
from django.views.generic import TemplateView

from tree.apps import TreeConfig

app_name = TreeConfig.name

urlpatterns = [
    # main_menu
    path('', TemplateView.as_view(template_name='index.html'), name='home_page'),
    path('products/', TemplateView.as_view(template_name='index.html'), name='products_page'),
    path('products/category/', TemplateView.as_view(template_name='index.html'), name='products_page'),
    path('favorites/', TemplateView.as_view(template_name='index.html'), name='favorites_page'),
    path('cart/', TemplateView.as_view(template_name='index.html'), name='cart_page'),

    # under_menu
    path('about/', TemplateView.as_view(template_name='index.html'), name='about_page'),
    path('about/team/', TemplateView.as_view(template_name='index.html'), name='team_page'),
    path('about/team/members/', TemplateView.as_view(template_name='index.html'), name='team_member_page')
]
